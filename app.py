import json
import sys
import pandas as pd
import requests
import streamlit as st

from const import COLUMNS, INDEX, HIDDEN, DROP, ITEMS, BS, PL, CF, ASSETS, LIABILITITES, NET_ASSETS, PL_ABST, COST_DETAILS, SGA_DETAILS, SGA_DROP, DEFAULT_URL ,DEVELOP_URL ,LATEST_URL,STAGING_URL

st.set_page_config(
    layout="wide"
)

st.title("不正会計検知AIシステム（内部版）")

# セッション状態の初期化
session_states = {
    "url": DEFAULT_URL,
    "file": None,
    "df": None,
    "hidden": None,
    "selected": [],
    "resp": None,
    "val_ready": False,
    "input_df": None,
    "user_code": "",
    "api_key": ""
}

for k, v in session_states.items():
    if k not in st.session_state:
        st.session_state[k] = v

with st.expander("API 接続先 URL"):
    # 環境選択
    env_options = {
        "DEFAULT": DEFAULT_URL,
        "DEVELOP": DEVELOP_URL,
        "LATEST": LATEST_URL,
        "STAGING": STAGING_URL
    }
    
    selected_env = st.selectbox(
        "環境を選択",
        options=list(env_options.keys()),
        index=0,
        help="使用するAPI環境を選択してください"
    )
    
    st.session_state["url"] = env_options[selected_env]
    
    # 現在のURL表示
    st.code(f"接続先: {st.session_state['url']}")


def init_data(items, default=0, unit="円"):
    """ 入力データの初期化"""
    return pd.DataFrame(dict(map(lambda item: (item, {"value": default, "unit": unit}), items))).T


def validate(user_code, api_key):
    """ ユーザー名とAPIキーの検証"""
    url = f"{st.session_state['url']}validate_key"
    params = {"user_code": user_code, "api_key": api_key}
    return requests.get(url=url, params=params)


def infer_single(record, user_code, api_key, _format="prob", _threshold=0.5):
    """ 不正会計確率の計算結果の取得（単一レコード）"""
    url = st.session_state["url"] + "infer_fraud"
    params = {"format": _format, "threshold": _threshold, "user_code": user_code}
    headers = {"X-API-KEY": api_key}
    items_map = dict(map(lambda item: (item["ja"], item["en"]), ITEMS["versions"][0]["items"]))
    data = list(map(lambda item: {"name": items_map[item[0]], "value": item[1]}, record.items()))
    payload = {"n_items": len(data), "version": ITEMS["versions"][0]["name"], "items": data}
    return requests.post(url=url, data=json.dumps(payload), params=params, headers=headers)


def infer_multi(records, user_codes, api_keys, _format="prob,level,binary", _threshold=0.5):
    """ 不正会計確率の計算結果の取得（複数レコード）"""
    url = st.session_state["url"] + "infer_fraud/multi"
    # 複数レコードでも最初のユーザーコードとAPIキーを使用
    params = {"format": _format, "threshold": _threshold, "user_code": user_codes[0]}
    headers = {"X-API-KEY": api_keys[0]}
    
    items_map = dict(map(lambda item: (item["ja"], item["en"]), ITEMS["versions"][0]["items"]))
    instances = []
    
    for record in records:
        items = list(map(lambda item: {"name": items_map[item[0]], "value": item[1]}, record.items()))
        instances.append({"items": items})
    
    payload = {
        "n_instances": len(instances),
        "n_items": len(instances[0]["items"]) if instances else 0,
        "version": ITEMS["versions"][0]["name"],
        "instances": instances
    }

    with open("./data/sent_payload.json", "w") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)

    return requests.post(url=url, data=json.dumps(payload), params=params, headers=headers)


# 入力（タブで分割）
with st.container(border=True,width='stretch'):
    upload_tab, input_tab = st.tabs(["ファイルアップロード", "画面入力"])

# ファイルアップロード
with upload_tab:
    st.session_state["file"] = st.file_uploader(label="財務情報ファイルを選択して「データ確認」ボタンを押してください。", 
                                              type=[".csv", ".xlsx"])

    def delete_file():
        st.session_state["file"] = None

    if st.button("データ確認", disabled=st.session_state["file"] is None, 
              help="ファイルのアップロードを行った後にクリックしてください。"):
        try:
            # ファイルの拡張子に応じて読み込み方法を切り替える
            file_extension = st.session_state["file"].name.split('.')[-1].lower()
            
            if file_extension == 'csv':
                df = pd.read_csv(st.session_state["file"])
            elif file_extension == 'xlsx':
                df = pd.read_excel(st.session_state["file"])
            else:
                st.error("サポートされていないファイル形式です。CSVまたはExcelファイルを選択してください。")
                delete_file()
                st.stop()
                
            if df.columns.to_list() == COLUMNS:
                df = df.set_index(INDEX)
                hidden = df[HIDDEN]
                df = df.drop(columns=HIDDEN + DROP).fillna(0).astype(int)
                st.session_state["df"] = df
                st.session_state["hidden"] = hidden
                delete_file()
            else:
                st.error("ファイル形式が間違っています。正しい列名を持つファイルを選択してください。")
        except Exception as e:
            st.error(f"ファイル読み込みエラー: {str(e)}")
            delete_file()

    if st.session_state["df"] is not None:
        with st.expander("詳細を表示", expanded=True):
            with st.container(height=500):
                # データフレームの表示用に加工
                display_df = st.session_state["df"].T.copy()
                
                # ヘッダーを会社名/会社番号/決算期の形式に変更
                new_columns = []
                for col in display_df.columns:
                    if isinstance(col, tuple) and len(col) >= 6:
                        # タプル形式: (メモ, 企業番号, 企業名, 所在地, 連絡先, 決算期, ...)
                        company_name = col[2]  # 企業名
                        company_code = col[1]  # 企業番号
                        period = col[5]  # 決算期
                        new_header = f"{period}/{company_name}/{company_code}"
                        new_columns.append(new_header)
                    else:
                        new_columns.append(str(col))
                
                display_df.columns = new_columns
                
                # カラム幅の設定とデータフレーム表示
                st.dataframe(
                    display_df,
                    width='stretch',  # コンテナ幅を最大限活用
                    height=450,  # コンテナ内での高さ調整
                    column_config={
                        col: st.column_config.Column(
                            width="medium",  # カラム幅を適切に設定
                            help=f"企業: {col}"
                        ) for col in display_df.columns
                    }
                )
        
        # セレクトボックス用の選択肢を作成（決算期：企業番号：企業名）
        options = []
        option_mapping = {}
        
        for idx in st.session_state["df"].index:
            if isinstance(idx, tuple) and len(idx) >= 7:
                # タプル形式のインデックス: (メモ, 企業番号, 企業名, 所在地, 連絡先, 決算期, 入力単位, 処理年度)
                display_text = f"{idx[5]}：{idx[2]}：{idx[1]}"  # 決算期：企業番号：企業名
                options.append(display_text)
                option_mapping[display_text] = idx
            else:
                # その他の形式の場合はそのまま使用
                display_text = str(idx)
                options.append(display_text)
                option_mapping[display_text] = idx
        
        # 全て選択機能のチェックボックス
        select_all = st.checkbox("全て選択", help="すべての企業決算期を一括選択します")
        
        # 複数選択に変更
        if select_all:
            # 全て選択された場合
            selected_display = st.multiselect(
                "確率を計算する企業決算期を選んで「予測」ボタンを押してください（複数選択可）",
                options,
                default=options,  # 全ての選択肢をデフォルトで選択
                help="複数の決算期を選択することで、一度に複数企業の不正会計確率を計算できます。")
        else:
            # 通常の選択
            selected_display = st.multiselect(
                "確率を計算する企業決算期を選んで「予測」ボタンを押してください（複数選択可）",
                options,
                help="複数の決算期を選択することで、一度に複数企業の不正会計確率を計算できます。")
        
        # 表示名から元のインデックスに変換
        st.session_state["selected"] = [option_mapping[display] for display in selected_display]

        # 閾値選択
        threshold = st.slider(
            "不正判定の閾値を選択してください", 
            min_value=0.0, 
            max_value=1.0, 
            value=0.5, 
            step=0.01,
            format="%.2f",
            help="この値以上の不正確率の場合に「不正判定: 有」となります"
        )

    if st.button("予測", disabled=not st.session_state["selected"], 
              help="予測対象の決算期を選んでからクリックしてください。"):
        
        with st.spinner("サーバーと通信中です。"):
            selected_records = []
            user_codes = []
            api_keys = []
            
            # 選択された各レコードの情報を取得
            for selected_idx in st.session_state["selected"]:
                record = st.session_state["df"].loc[selected_idx].to_dict()
                selected_records.append(record)
                
                # 対応するUID、APIキーを取得
                hidden_row = st.session_state["hidden"].loc[selected_idx]
                user_codes.append(hidden_row["UID"])
                api_keys.append(hidden_row["APIキー"])
            
            # レコード数によってAPIエンドポイントを切り替え
            if len(selected_records) == 1:
                st.session_state["resp"] = infer_single(
                    selected_records[0], 
                    user_codes[0], 
                    api_keys[0],
                    _threshold=threshold
                )
            else:
                st.session_state["resp"] = infer_multi(
                    selected_records, 
                    user_codes,
                    api_keys,
                    _threshold=threshold
                )

# 画面入力
with input_tab:
    cols = st.columns(2)
    
    with cols[0]:
        st.session_state["user_code"] = st.text_input("ユーザーコード")
    with cols[1]:
        st.session_state["api_key"] = st.text_input("APIキー", type="password", autocomplete="")
    enable_button = bool(st.session_state["user_code"].strip()) and bool(st.session_state["api_key"].strip())  
    unit = st.selectbox("単位", ["円", "千円", "百万円", "十億円"])
    item_name_conf = st.column_config.Column(
                                    "勘定科目名",
                                    width="medium",
                                    disabled=True
                                )
    value_conf = st.column_config.NumberColumn(
                                    "計上額",
                                    width=None,
                                    format="localized",
                                    step=1
                                )
    unit_conf = st.column_config.Column(
                                    "単位",
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
                assets = st.data_editor(init_data(ASSETS,unit=unit),
                            width='stretch',
                            height=height-offsets[0],
                            column_config={
                                "_index": item_name_conf,
                                "value": value_conf,
                                "unit": unit_conf
                            })
        with bs_cols[1]:
            st.write("貸方")
            with st.container(height=int(height/2)):
                st.write("負債の部")
                liabilities = st.data_editor(init_data(LIABILITITES,unit=unit),
                            width='stretch',
                            height=int(height/2)-offsets[1],
                            column_config={
                                "_index": item_name_conf,
                                "value": value_conf,
                                "unit": unit_conf
                            })
            with st.container(height=int(height/2)):
                st.write("純資産の部")
                net_assets = st.data_editor(init_data(NET_ASSETS,unit=unit),
                            width='stretch',
                            height=int(height/2)-offsets[1],
                            column_config={
                                "_index": item_name_conf,
                                "value": value_conf,
                                "unit": unit_conf
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
                pl_abst = st.data_editor(init_data(PL_ABST,unit=unit),
                            width='stretch',
                            height=height-offsets[0],
                            column_config={
                                "_index": item_name_conf,
                                "value": value_conf,
                                "unit": unit_conf
                            })
        with pl_cols[1]:
            with st.container(height=int(height/2)):
                st.write("原価明細")
                cost_details = st.data_editor(init_data(COST_DETAILS,unit=unit),
                            width='stretch',
                            height=int(height/2)-offsets[1],
                            column_config={
                                "_index": item_name_conf,
                                "value": value_conf,
                                "unit": unit_conf
                            })
            with st.container(height=int(height/2)):
                st.write("販管費明細")
                sga_details_cols = list(filter(lambda item:item not in SGA_DROP, SGA_DETAILS))
                sga_details = st.data_editor(init_data(sga_details_cols,unit=unit),
                            width='stretch',
                            height=int(height/2)-offsets[1],
                            column_config={
                                "_index": item_name_conf,
                                "value": value_conf,
                                "unit": unit_conf
                            })
        pl = pd.concat([pl_abst, cost_details, sga_details], axis="rows")
    with st.expander("キャッシュ・フロー計算書"):
        height = 500
        margin = 20
        offsets = (60, 80)
        with st.container(height=height):
            cf = st.data_editor(init_data(CF,unit=unit),
                        width='stretch',
                        height=int(height)-offsets[0],
                        column_config={
                            "_index": item_name_conf,
                            "value": value_conf,
                            "unit": unit_conf
                        })
    full_df = pd.concat([bs, pl, cf], axis="rows")
    full_df = full_df.loc[:, ["value"]].T
    full_df.index = [0]

    st.session_state["input_df"] = full_df

    if st.session_state["input_df"] is not None:
        # 閾値選択
        input_threshold = st.slider(
            "不正判定の閾値を選択してください", 
            min_value=0.0, 
            max_value=1.0, 
            value=0.5, 
            step=0.01,
            format="%.2f",
            help="この値以上の不正確率の場合に「不正判定: 有」となります",
            key="input_threshold"
        )
        
        if st.button("送信", disabled=not enable_button, help="データを送信するためには、ユーザーコードとAPIキーを入力してください。"):

            with st.spinner("ユーザー情報の認証中です。"):
                resp = validate(st.session_state["user_code"], st.session_state["api_key"])
            data = json.loads(resp.content)
            if resp.status_code == 200 and data["result"]:
                with st.spinner("確率の予測中です。"):
                    items = dict(map(lambda item:(item["ja"], item["en"]), ITEMS["versions"][0]["items"]))
                    record = st.session_state["input_df"].loc[0].to_dict()
                    st.session_state["resp"] = None
                    st.session_state["resp"] = infer_single(
                        record, 
                        st.session_state["user_code"], 
                        st.session_state["api_key"],
                        _threshold=input_threshold
                    )
            else:
                st.session_state["resp"] = None
                resp.status_code = 400
                st.session_state["resp"] = resp

# 結果の表示（全タブで共通）
with st.container(border=True):
    st.write("## 結果")
    if st.session_state["resp"] is not None:
        status = st.session_state["resp"].status_code
        if status == 200:
            data = json.loads(st.session_state["resp"].content)
            
            # 単一レコードの場合
            if "probability" in data:
                prob = data["probability"]
                level = data.get("level", "")
                binary = "有" if data.get("binary", False) else "無"
                
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric(label="不正確率", value=f"{prob*100:0.2f}%")
                with col2:
                    st.metric(label="リスクレベル", value=level)
                with col3:
                    st.metric(label="不正判定", value=binary)
                    
            # 複数レコードの場合
            elif "predictions" in data:
                predictions = data["predictions"]
                results = []
                
                for i, prediction in enumerate(predictions):
                    # インデックス情報を取得
                    if i < len(st.session_state["selected"]):
                        selected_key = st.session_state["selected"][i]
                        # タプルの場合は「企業名・決算期」形式に変換
                        if isinstance(selected_key, tuple) and len(selected_key) >= 6:
                            display_key = f"{selected_key[2]}・{selected_key[5]}"  # 企業名・決算期
                        else:
                            display_key = str(selected_key)
                    else:
                        display_key = f"レコード{i+1}"
                    
                    prob = prediction.get("probability", 0)
                    level = prediction.get("level", "")
                    binary = "有" if prediction.get("binary", False) else "無"
                    
                    results.append({
                        "企業決算期": display_key,
                        "不正確率": f"{prob*100:0.2f}%",
                        "リスクレベル": level,
                        "不正判定": binary
                    })
                
                results_df = pd.DataFrame(results)
                st.dataframe(results_df, width='stretch')
                
                # 統計情報の表示
                if len(results) > 1:
                    st.write("### 統計情報")
                    probs = [prediction.get("probability", 0) for prediction in predictions]
                    avg_prob = sum(probs) / len(probs)
                    max_prob = max(probs)
                    min_prob = min(probs)
                    fraud_count = sum(1 for prediction in predictions if prediction.get("binary", False))
                    
                    col1, col2, col3, col4 = st.columns(4)
                    with col1:
                        st.metric("平均不正確率", f"{avg_prob*100:.2f}%")
                    with col2:
                        st.metric("最高不正確率", f"{max_prob*100:.2f}%")
                    with col3:
                        st.metric("最低不正確率", f"{min_prob*100:.2f}%")
                    with col4:
                        st.metric("不正判定件数", f"{fraud_count}/{len(results)}")
                
        elif status == 504:
            st.error("サーバーの処理がタイムアウトしました。もう一度「予測」ボタンを押してください。")
        else:
            st.error(f"エラーが発生しました (ステータスコード: {status})")
            try:
                error_data = json.loads(st.session_state["resp"].content)
                if "detail" in error_data:
                    st.error(f"詳細: {error_data['detail']}")
                else:
                    st.error(f"レスポンス: {error_data}")
            except:
                st.error(f"レスポンス: {st.session_state['resp'].content}")
