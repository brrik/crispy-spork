import streamlit as st
import requests
import pandas as pd
from color import sentiment_color
# ユーザーID、パスワード、および役職の辞書（役職情報を追加）
#USER_CREDENTIALS = {
    #"Tomiyasu": {"password": "First", "role": "部長"},
    #"Ryo": {"password": "Last", "role": "課長"},
    #"user3": {"password": "Pass123", "role": "GL"},
#}

def login():
    st.title("ログイン画面")

    # ユーザーIDとパスワードの入力欄
    username = st.text_input("ユーザーID")
    password = st.text_input("パスワード", type="password")
    

    

    # ログインボタン
    if st.button("ログイン"):
        url = "https://altxfastapi-test.onrender.com/login/"
        res = requests.get(url + username + "/" +password)
        data = res.json()
        if data != False:
            st.session_state["authenticated"] = True
            st.session_state["username"] = username
            st.session_state["role"] = data
            print(data)
            st.success(f"ログイン成功: ようこそ {username} さん！")
            st.rerun()
        else:
            st.error("ユーザーIDまたはパスワードが間違っています")


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


    url = "https://altxfastapi-test.onrender.com/getrolldata/"
    st.title("メインページ")
    columns = ["日時", "役職", "投稿内容", "感情分析", "得点1", "得点2", "得点3", "得点4", "得点5"]
    # ユーザーの役職によって表示内容を変更
    if st.session_state["role"] == "社長":
        st.write("社長専用のコンテンツ")
        res = requests.get(url + "sh")
        data = res.json()
        df = pd.DataFrame(data, columns=columns)
        df = df.drop(df.columns[-5:], axis=1)
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
        styler = current_data.style.map(sentiment_color, subset=["感情分析"])
        # 表示
        st.write(f"ページ {st.session_state.current_page} / {total_pages}")
        st.dataframe(styler, use_container_width=True)

        # 前のページボタン
        col1, col2, col3 = st.columns([1, 2, 1])  # ボタン位置調整
        if col1.button("前のページ") and st.session_state.current_page > 1:
            st.session_state.current_page -= 1

        # 次のページボタン
        if col3.button("次のページ") and st.session_state.current_page < total_pages:
            st.session_state.current_page += 1
        #st.write(df)
        # 社長向けの追加情報やアクション

    elif st.session_state["role"] == "事業部長":
        st.write("事業部長専用のコンテンツ")
        res = requests.get(url + "jb")
        data = res.json()
        df = pd.DataFrame(data, columns=columns)
        df = df.drop(df.columns[-5:], axis=1)
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
        styler = current_data.style.map(sentiment_color, subset=["感情分析"])
        # 表示
        st.write(f"ページ {st.session_state.current_page} / {total_pages}")
        st.dataframe(styler, use_container_width=True)

        # 前のページボタン
        col1, col2, col3 = st.columns([1, 2, 1])  # ボタン位置調整
        if col1.button("前のページ") and st.session_state.current_page > 1:
            st.session_state.current_page -= 1

        # 次のページボタン
        if col3.button("次のページ") and st.session_state.current_page < total_pages:
            st.session_state.current_page += 1
        #st.write(df)
        # 社長向けの追加情報やアクション
    
    elif st.session_state["role"] == "部長":
        st.write("部長専用のコンテンツ")
        res = requests.get(url + "bc")
        data = res.json()
        df = pd.DataFrame(data, columns=columns)
        df = df.drop(df.columns[-5:], axis=1)
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
        styler = current_data.style.map(sentiment_color, subset=["感情分析"])
        # 表示
        st.write(f"ページ {st.session_state.current_page} / {total_pages}")
        st.dataframe(styler, use_container_width=True)

        # 前のページボタン
        col1, col2, col3 = st.columns([1, 2, 1])  # ボタン位置調整
        if col1.button("前のページ") and st.session_state.current_page > 1:
            st.session_state.current_page -= 1

        # 次のページボタン
        if col3.button("次のページ") and st.session_state.current_page < total_pages:
            st.session_state.current_page += 1
        # 部長向けの追加情報やアクション    

    elif st.session_state["role"] == "課長":
        st.write("課長専用のコンテンツ")
        res = requests.get(url + "kc")
        data = res.json()
        df = pd.DataFrame(data, columns=columns)
        df = df.drop(df.columns[-5:], axis=1)
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
        styler = current_data.style.map(sentiment_color, subset=["感情分析"])
        # 表示
        st.write(f"ページ {st.session_state.current_page} / {total_pages}")
        st.dataframe(styler, use_container_width=True)

        # 前のページボタン
        col1, col2, col3 = st.columns([1, 2, 1])  # ボタン位置調整
        if col1.button("前のページ") and st.session_state.current_page > 1:
            st.session_state.current_page -= 1

        # 次のページボタン
        if col3.button("次のページ") and st.session_state.current_page < total_pages:
            st.session_state.current_page += 1
        # 課長向けの追加情報やアクション
    elif st.session_state["role"] == "GL":
        st.write("GL専用のコンテンツ")
        res = requests.get(url + "gl")
        data = res.json()
        df = pd.DataFrame(data, columns=columns)
        df = df.drop(df.columns[-5:], axis=1)
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
        styler = current_data.style.map(sentiment_color, subset=["感情分析"])
        # 表示
        st.write(f"ページ {st.session_state.current_page} / {total_pages}")
        st.dataframe(styler, use_container_width=True)

        # 前のページボタン
        col1, col2, col3 = st.columns([1, 2, 1])  # ボタン位置調整
        if col1.button("前のページ") and st.session_state.current_page > 1:
            st.session_state.current_page -= 1

        # 次のページボタン
        if col3.button("次のページ") and st.session_state.current_page < total_pages:
            st.session_state.current_page += 1
        # GL向けの追加情報やアクション
