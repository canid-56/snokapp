import json
import sys

import pandas as pd
import requests
import streamlit as st

from const import COLUMNS, INDEX, HIDDEN, DROP, ITEMS

st.title("不正会計検知AIシステム（内部版）")
# st.write(sys.version)

if "file" not in st.session_state:
    st.session_state["file"] = None

if "df" not in st.session_state:
    st.session_state["df"] = None

if "hidden" not in st.session_state:
    st.session_state["hidden"] = None

if "selected" not in st.session_state:
    st.session_state["selected"] = None

if "resp" not in st.session_state:
    st.session_state["resp"] = None

st.session_state["file"] = accountings_file = st.file_uploader(label="財務情報ファイルを選択して「データ確認」ボタンを押してください。", type=".csv")


if st.button("データ確認", disabled=st.session_state["file"] is None):
    df = pd.read_csv(st.session_state["file"])
    if df.columns.to_list() == COLUMNS:
        df = df.set_index(INDEX)
        hidden = df[HIDDEN]
        df = df.drop(columns=HIDDEN + DROP).fillna(0).astype(int)
        # st.table(df.T)
        st.session_state["df"] = df
        st.session_state["hidden"] = hidden
        st.session_state["file"] = None
    else:
        st.write("ファイル形式が間違っています")

if st.session_state["df"] is not None:
    with st.expander("表示切り替え", expanded=True):
        with st.container(height=600):
            st.table(st.session_state["df"].T)
    st.session_state["selected"] = st.selectbox("確率を計算する企業決算期を選んで「予測」ボタンを押してください。",
                            st.session_state["df"].index,
                            index=None, placeholder="選択")

if st.button("予測", disabled=st.session_state["selected"] is None):
    # st.write(st.session_state["selected"])
    index = dict(zip(INDEX, st.session_state["selected"]))
    hidden = st.session_state["hidden"].loc[st.session_state["selected"]].to_dict()
    # st.write(index)
    # st.write(hidden)
    url = "https://3geeggzw92.execute-api.ap-northeast-1.amazonaws.com/staging/infer_fraud"
    params = {"format":"prob", "threshold":0.5, "user_code":hidden["UID"]}
    headers = {"X-API-KEY":hidden["APIキー"]}
    # from const import EXAMPLE
    # body = EXAMPLE
    with st.spinner("サーバーと通信中です。"):
        items = dict(map(lambda item:(item["ja"], item["en"]), ITEMS["versions"][0]["items"]))
        record = st.session_state["df"].loc[st.session_state["selected"]].to_dict()
        # st.write(items)
        # st.write(record)
        data = list(map(lambda item:{"name":items[item[0]], "value":item[1]}, record.items()))
        # st.write(data)
        payload = {"n_items":len(data), "version":ITEMS["versions"][0]["name"], "items":data}
        # st.write(payload)
        st.session_state["resp"] = None
        st.session_state["resp"] = requests.post(url=url, data=json.dumps(payload), params=params, headers=headers)

if st.session_state["resp"] is not None:
    status = st.session_state["resp"].status_code
    if status == 200:
        data = json.loads(st.session_state["resp"].content)
        prob = data["probability"]
        # st.write(data)
        st.metric(label="不正確率", value=f"{prob*100:0.2f}%")
    elif status == 504:
        st.write("サーバーの処理がタイムアウトしました。もう一度「予測」ボタンを押してください。")
    else:
        st.write(st.session_state["resp"].content)