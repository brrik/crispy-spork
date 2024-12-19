import streamlit as st

#ユーザーID、パスワード、および役職の辞書（役職情報を追加）
USER_CREDENTIALS = {
    "Tomiyasu": {"password": "First", "role": "部長"},
    "Ryo": {"password": "Last", "role": "課長"},
    "user3": {"password": "Pass123", "role": "GL"},
}

def login():
    st.title("ログイン画面")

    # ユーザーIDとパスワードの入力欄
    username = st.text_input("ユーザーID")
    password = st.text_input("パスワード", type="password")

    # ログインボタン
    if st.button("ログイン"):
        if username in USER_CREDENTIALS and USER_CREDENTIALS[username]["password"] == password:
            st.session_state["authenticated"] = True
            st.session_state["username"] = username
            st.session_state["role"] = USER_CREDENTIALS[username]["role"]
            st.success(f"ログイン成功: ようこそ {username} さん！")
            st.rerun()
        else:
            st.error("ユーザーIDまたはパスワードが間違っています")

#認証済みかどうか確認
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if not st.session_state["authenticated"]:
    login()
else:
    # サイドバーにユーザー名と役職を表示
    st.sidebar.title("メニュー")
    st.sidebar.write(f"ようこそ、{st.session_state['username']} さん ({st.session_state['role']})")
    st.sidebar.button("ログアウト", on_click=lambda: st.session_state.update({"authenticated": False}))

    # メインページのコンテンツ
    import requests

    url = "https://pythonapi-egwh.onrender.com/getrolldata/"
    st.title("メインページ")
    
    #ユーザーの役職によって表示内容を変更
    if st.session_state["role"] == "部長":
        st.write("部長専用のコンテンツ")
        res = requests.get(url + "bc")
        data = res.json()
        st.write(data)
        # 部長向けの追加情報やアクション
    elif st.session_state["role"] == "課長":
        st.write("課長専用のコンテンツ")
        res = requests.get(url + "kc")
        data = res.json()
        st.write(data)
        # 課長向けの追加情報やアクション
    elif st.session_state["role"] == "GL":
        st.write("GL専用のコンテンツ")
        res = requests.get(url + "gl")
        data = res.json()
        st.write(data)
        # GL向けの追加情報やアクション