import streamlit as st

# ユーザーIDとパスワードの辞書（簡易的な認証用）
USER_CREDENTIALS = {
    "user1": "password1",
    "user2": "password2"
}

def login():
    st.title("ログイン画面")

    # ユーザーIDとパスワードの入力欄
    username = st.text_input("ユーザーID")
    password = st.text_input("パスワード", type="password")

    # ログインボタン
    if st.button("ログイン"):
        if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
            st.session_state["authenticated"] = True
            st.session_state["username"] = username
            st.success(f"ログイン成功: ようこそ {username} さん！")
            st.experimental_rerun()
        else:
            st.error("ユーザーIDまたはパスワードが間違っています")

# 認証済みかどうか確認
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if not st.session_state["authenticated"]:
    login()
else:
    st.sidebar.title("メニュー")
    st.sidebar.write(f"ようこそ、{st.session_state['username']} さん")
    st.sidebar.button("ログアウト", on_click=lambda: st.session_state.update({"authenticated": False}))

    # メインページのコンテンツ
    st.title("メインページ")
    st.write("ここにWEBアプリのメインコンテンツを表示します")