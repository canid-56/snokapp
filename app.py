import json
import sys

import pandas as pd
import requests
import streamlit as st

from const import COLUMNS, INDEX, HIDDEN, DROP, ITEMS, BS, PL, CF, ASSETS, LIABILITITES, NET_ASSETS, PL_ABST, COST_DETAILS, SGA_DETAILS, SGA_DROP

st.title("不正会計検知AIシステム（内部版）")

# セッション状態の初期化
session_states = {
    "file":None,
    "df":None,
    "hidden":None,
    "selected":None,
    "resp":None,
    "val_ready":False,
    "input_df":None,
    "user_code":"",
    "api_key":""
}

for k,v in session_states.items():
    if k not in st.session_state:
        st.session_state[k] = v

with st.container(border=True):

    # upload_tab, input_tab, validate_tab = st.tabs(["ファイルアップロード", "画面入力", "APIキー検証"])
    upload_tab, input_tab = st.tabs(["ファイルアップロード", "画面入力"])

# with validate_tab:
#     cols = st.columns(2)
    
    # with cols[0]:
    #     user_code = st.text_input("ユーザーコード")
    # with cols[1]:
    #     api_key = st.text_input("APIキー", type="password", autocomplete="")
    # enable_button = bool(user_code.strip()) and bool(api_key.strip())         
    # # st.session_state["val_ready"] = len(user_code) > 0 & len(api_key) > 0
    # if st.button("検証", disabled=not enable_button):
    #     # st.write(f"user_code : {user_code}, api_key : {api_key}")
    #     url = "https://3geeggzw92.execute-api.ap-northeast-1.amazonaws.com/staging/validate_key"
    #     params = {"user_code":user_code, "api_key":api_key}
    #     with st.spinner("サーバーと通信中です。"):
    #         resp = requests.get(url=url, params=params)
    #         # st.write(resp.content)
    #         data = json.loads(resp.content)
    #     if resp.status_code == 200:
    #         # st.write(data)
    #         if data["result"]:
    #             st.success(data["message"], icon="✅")
    #         else:
    #             st.error(data["message"], icon="❌")

def validate(user_code, api_key):
    url = "https://3geeggzw92.execute-api.ap-northeast-1.amazonaws.com/staging/validate_key"
    params = {"user_code":user_code, "api_key":api_key}
    resp = requests.get(url=url, params=params)
    return resp
    # data = json.loads(resp.content)
    # return resp.status_code, data

with upload_tab:

    st.session_state["file"] = st.file_uploader(label="財務情報ファイルを選択して「データ確認」ボタンを押してください。", type=".csv")

    def delete_file():
        st.session_state["file"] = None

    if st.button("データ確認", disabled=st.session_state["file"] is None, help="ファイルのアップロードを行った後にクリックしてください。"):
        df = pd.read_csv(st.session_state["file"])
        if df.columns.to_list() == COLUMNS:
            df = df.set_index(INDEX)
            hidden = df[HIDDEN]
            df = df.drop(columns=HIDDEN + DROP).fillna(0).astype(int)
            st.session_state["df"] = df
            st.session_state["hidden"] = hidden
            # st.session_state["file"] = None
            delete_file()
        else:
            st.write("ファイル形式が間違っています")

    if st.session_state["df"] is not None:
        with st.expander("表示切り替え", expanded=True):
            with st.container(height=600):
                st.table(st.session_state["df"].T)
        st.session_state["selected"] = st.selectbox("確率を計算する企業決算期を選んで「予測」ボタンを押してください。",
                                st.session_state["df"].index,
                                index=None, placeholder="選択")

    if st.button("予測", disabled=st.session_state["selected"] is None, help="予測対象の決算期を選んでからクリックしてください。"):

        index = dict(zip(INDEX, st.session_state["selected"]))
        hidden = st.session_state["hidden"].loc[st.session_state["selected"]].to_dict()
    
        url = "https://3geeggzw92.execute-api.ap-northeast-1.amazonaws.com/staging/infer_fraud"
        params = {"format":"prob", "threshold":0.5, "user_code":hidden["UID"]}
        headers = {"X-API-KEY":hidden["APIキー"]}
        with st.spinner("サーバーと通信中です。"):
            items = dict(map(lambda item:(item["ja"], item["en"]), ITEMS["versions"][0]["items"]))
            record = st.session_state["df"].loc[st.session_state["selected"]].to_dict()
            data = list(map(lambda item:{"name":items[item[0]], "value":item[1]}, record.items()))
            payload = {"n_items":len(data), "version":ITEMS["versions"][0]["name"], "items":data}
            st.session_state["resp"] = None
            st.session_state["resp"] = requests.post(url=url, data=json.dumps(payload), params=params, headers=headers)



def init_data(items, default=0, unit="円"):
    return pd.DataFrame(dict(map(lambda item:(item, {"value":default,"unit":unit}), items))).T


with input_tab:
    cols = st.columns(2)
    
    with cols[0]:
        st.session_state["user_code"] = st.text_input("ユーザーコード")
    with cols[1]:
        st.session_state["api_key"] = st.text_input("APIキー", type="password", autocomplete="")
    enable_button = bool(st.session_state["user_code"].strip()) and bool(st.session_state["api_key"].strip())  
    unit = st.selectbox("単位",["円","千円","百万円","十億円"])
    item_name_conf = st.column_config.Column(
                                    "勘定科目名",
                                    width="medium",
                                    disabled=True
                                )
    value_conf = st.column_config.NumberColumn(
                                    "計上額",
                                    # width="small",
                                    width=None,
                                    format="localized",
                                    step=1
                                )
    unit_conf = st.column_config.Column(
                                    "単位",
                                    # width="small",
                                    width="small",
                                    disabled=True
                                )
    with st.expander("貸借対照表"):
        bs_cols = st.columns(2)
        height = 500
        margin = 20
        offsets = (60, 80)
        with bs_cols[0]:
            st.write("借方")
            with st.container(height=height+margin):
                st.write("資産の部")
                # st.write(BS)
                assets = st.data_editor(init_data(ASSETS,unit=unit),
                            use_container_width=True,
                            height=height-offsets[0],
                            column_config={
                                "_index":item_name_conf,
                                "value":value_conf,
                                "unit":unit_conf
                            })
        with bs_cols[1]:
            st.write("貸方")
            with st.container(height=int(height/2)):
                st.write("負債の部")
                liabilities = st.data_editor(init_data(LIABILITITES,unit=unit),
                            use_container_width=True,
                            height=int(height/2)-offsets[1],
                            column_config={
                                "_index":item_name_conf,
                                "value":value_conf,
                                "unit":unit_conf
                            })
            with st.container(height=int(height/2)):
                st.write("純資産の部")
                net_assets = st.data_editor(init_data(NET_ASSETS,unit=unit),
                            use_container_width=True,
                            height=int(height/2)-offsets[1],
                            column_config={
                                "_index":item_name_conf,
                                "value":value_conf,
                                "unit":unit_conf
                            })
        bs = pd.concat([assets, liabilities, net_assets], axis="rows")
    with st.expander("損益計算書"):
        pl_cols = st.columns(2)
        height = 500
        margin = 20
        offsets = (60, 80)
        with pl_cols[0]:
            with st.container(height=height+margin):
                st.write("損益計算書")
                # st.write(PL)
                pl_abst = st.data_editor(init_data(PL_ABST,unit=unit),
                            use_container_width=True,
                            height=height-offsets[0],
                            column_config={
                                "_index":item_name_conf,
                                "value":value_conf,
                                "unit":unit_conf
                            })
        with pl_cols[1]:
            with st.container(height=int(height/2)):
                st.write("原価明細")
                cost_details = st.data_editor(init_data(COST_DETAILS,unit=unit),
                            use_container_width=True,
                            height=int(height/2)-offsets[1],
                            column_config={
                                "_index":item_name_conf,
                                "value":value_conf,
                                "unit":unit_conf
                            })
            with st.container(height=int(height/2)):
                st.write("販管費明細")
                sga_details_cols = list(filter(lambda item:item not in SGA_DROP, SGA_DETAILS))
                # sga_details = st.data_editor(init_data(SGA_DETAILS,unit=unit),
                sga_details = st.data_editor(init_data(sga_details_cols,unit=unit),
                            use_container_width=True,
                            height=int(height/2)-offsets[1],
                            column_config={
                                "_index":item_name_conf,
                                "value":value_conf,
                                "unit":unit_conf
                            })
        pl = pd.concat([pl_abst, cost_details, sga_details], axis="rows")
    with st.expander("キャッシュ・フロー計算書"):
        height = 500
        margin = 20
        offsets = (60, 80)
        with st.container(height=height):
            # st.write("CF")
            cf = st.data_editor(init_data(CF,unit=unit),
                        use_container_width=True,
                        height=int(height)-offsets[0],
                        column_config={
                            "_index":item_name_conf,
                            "value":value_conf,
                            "unit":unit_conf
                        })
    full_df = pd.concat([bs, pl, cf], axis="rows")
    # full_df = full_df.loc[BS+PL+CF,["value"]].T
    full_df = full_df.loc[:,["value"]].T
    full_df.index = [0]
    # st.dataframe(full_df,
    #                 # column_config={
    #                 #     "_index":item_name_conf,
    #                 #     "value":value_conf,
    #                 #     "unit":unit_conf                     
    #                 # }
    #              )
    # if st.button("データ登録"):
    st.session_state["input_df"] = full_df

    if st.session_state["input_df"] is not None:
        if st.button("送信", disabled=not enable_button, help="データを送信するためには、ユーザーコードとAPIキーを入力してください。"):

            with st.spinner("ユーザー情報の認証中です。"):
                resp = validate(st.session_state["user_code"], st.session_state["api_key"])
            data = json.loads(resp.content)
            if resp.status_code == 200 and data["result"]:
                url = "https://3geeggzw92.execute-api.ap-northeast-1.amazonaws.com/staging/infer_fraud"
                params = {"format":"prob", "threshold":0.5, "user_code":st.session_state["user_code"]}
                headers = {"X-API-KEY":st.session_state["api_key"]}
                with st.spinner("確率の予測中です。"):
                    items = dict(map(lambda item:(item["ja"], item["en"]), ITEMS["versions"][0]["items"]))
                    record = st.session_state["input_df"].loc[0].to_dict()
                    data = list(map(lambda item:{"name":items[item[0]], "value":item[1]}, record.items()))
                    payload = {"n_items":len(data), "version":ITEMS["versions"][0]["name"], "items":data}
                    st.session_state["resp"] = None
                    st.session_state["resp"] = requests.post(url=url, data=json.dumps(payload), params=params, headers=headers)
            else:
                st.session_state["resp"] = None
                resp.status_code = 400
                st.session_state["resp"] = resp

with st.container(border=True):
    st.write("## 結果")
    if st.session_state["resp"] is not None:
        status = st.session_state["resp"].status_code
        if status == 200:
            data = json.loads(st.session_state["resp"].content)
            prob = data["probability"]
            st.metric(label="不正確率", value=f"{prob*100:0.2f}%")
        elif status == 504:
            st.write("サーバーの処理がタイムアウトしました。もう一度「予測」ボタンを押してください。")
        else:
            st.write(st.session_state["resp"].content)