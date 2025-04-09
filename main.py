import streamlit as st
import requests
import pandas as pd
from datetime import datetime
from color import sentiment_color
from graph import display_graph
from graph import display_graph_stacked

if not "loading" in st.session_state:
    st.session_state.loading = False

import streamlit as st
import requests

def login():
    st.title("ログイン画面")

    # セッションステートに初期値を設定
    if "loading" not in st.session_state:
        st.session_state.loading = False

    # ユーザーIDとパスワードの入力欄
    username = st.text_input("ユーザーID")
    password = st.text_input("パスワード", type="password")

    # ログイン処理関数
    def do_login():
        st.session_state.loading = True
        try:
            url = "https://pythonapi-egwh.onrender.com/login/"
            res = requests.get(url + username + "/" + password)
            data = res.json()

            if data != False:
                st.session_state["authenticated"] = True
                st.session_state["username"] = username
                st.session_state["role"] = data
                st.success(f"ログイン成功: ようこそ {username} さん！")
                st.rerun()
            else:
                st.error("ユーザーIDまたはパスワードが間違っています")
        except Exception as e:
            st.error(f"ログイン中にエラーが発生しました: {e}")
        finally:
            st.session_state.loading = False

    # ボタン表示（状態に応じて切り替える）
    if st.session_state.loading:
        st.button("ログイン中...", disabled=True)
    else:
        if st.button("ログイン"):
            do_login()

# 認証済みかどうか確認
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if not st.session_state["authenticated"]:
    login()
else:
    # サイドバーにユーザー名と役職を表示
    st.set_page_config(
        layout="wide",
        initial_sidebar_state="collapsed"
    )

    st.sidebar.title("メニュー")
    st.sidebar.write(f"ようこそ、{st.session_state['username']} さん ({st.session_state['role']})")
    st.sidebar.button("ログアウト", on_click=lambda: st.session_state.update({"authenticated": False}))

    # メインページのコンテンツ


    url = "https://pythonapi-egwh.onrender.com/getrolldata/"
    st.title("メインページ")
    columns = ["日時", "役職", "投稿内容", "感情", "非常にネガティブ", "ネガティブ", "ニュートラル", "ポジティブ", "非常にポジティブ"]
    if st.session_state["role"] == "社長":
        url2 = "sh"
    elif st.session_state["role"] == "事業部長":
        url2 = "jb"
    elif st.session_state["role"] == "部長":
        url2 = "bc"
    elif st.session_state["role"] == "課長":
        url2 = "kc"
    elif st.session_state["role"] == "GL":
        url2 = "gl"
    # ユーザーの役職によって表示内容を変更
    yakusyoku = st.session_state["role"]
    st.write(yakusyoku + "専用のコンテンツ")
    res = requests.get(url + url2)
    data = res.json()
    df = pd.DataFrame(data, columns=columns)
    df2 = pd.DataFrame(data, columns=columns)
    df = df.sort_values(by="日時", ascending=False)  # 最新の日付から表示
    df2 = df2.sort_values(by="日時", ascending=False)  # 最新の日付から表示
    df = df.drop(df.columns[-5:], axis=1)

    search_query = st.text_input("検索", "")

    # 検索機能
    if search_query:
        df = df[df.apply(lambda row: row.astype(str).str.contains(search_query).any(), axis=1)]
            
    # ページネーション設定
    items_per_page = 10
    total_pages = (len(df) + items_per_page - 1) // items_per_page

    # 現在のページをセッションステートで管理
    if "current_page" not in st.session_state:
        st.session_state.current_page = 1

    # 現在のページデータを取得
    start_index = (st.session_state.current_page - 1) * items_per_page
    end_index = start_index + items_per_page
    current_data = df.iloc[start_index:end_index]
    current_data2 = df2.iloc[start_index:end_index]
    styler = current_data.style.set_table_styles(
        [
            {"selector": "td", "props": [("white-space", "normal"), ("word-wrap", "break-word")]},
            {"selector": "th", "props": [("white-space", "normal"), ("word-wrap", "break-word")]},
            {"selector": "td:nth-child(4)", "props": [("width", "65%")]}
        ]
    ).map(
        sentiment_color, subset=["感情"]
    )
    # StreamlitでHTMLとして表示
    st.markdown(
        """
        <style>
        .dataframe td {
            vertical-align: top;  /* テキストを上に揃える */
        }
        .markdown-text {
            width: 100%;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # 表示
    st.write(f"ページ {st.session_state.current_page} / {total_pages}")
    #st.dataframe(styler, use_container_width=True)
    show_graph = st.checkbox("感情カテゴリの投稿件数を表示")
    show_graph_stacked = st.checkbox("感情スコアを表示")
    if show_graph:
        display_graph(data)

    if show_graph_stacked:
        display_graph_stacked(current_data2)

    st.markdown(styler.to_html(),
                unsafe_allow_html=True
                )
    # 前のページボタン
    col1, col2, col3 = st.columns([1, 2, 1])  # ボタン位置調整
    if col1.button("前のページ") and st.session_state.current_page > 1:
        st.session_state.current_page -= 1

    # 次のページボタン
    if col3.button("次のページ") and st.session_state.current_page < total_pages:
        st.session_state.current_page += 1
    #st.write(df)
    # 社長向けの追加情報やアクション

    