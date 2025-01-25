import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
import os

# 日本語フォント設定 (IPAexゴシック)
def set_japanese_font():
    # フォントファイルのパスを指定
    font_path = os.path.join(os.path.dirname(__file__), "ipaexg.ttf")  # フォントファイルをプロジェクトフォルダにアップロード
    try:
        font_prop = fm.FontProperties(fname=font_path)
        plt.rcParams['font.family'] = font_prop.get_name()
    except Exception as e:
        st.error("フォントの読み込みに失敗しました。")
        st.write(e)

# フォント設定を適用
font_prop = set_japanese_font()

def display_graph(data):
    # データフレームに変換
    df = pd.DataFrame(data, columns=["日時", "役職", "投稿内容", "感情", "非常にネガティブ", "ネガティブ", "ニュートラル", "ポジティブ", "非常にポジティブ"])
    # 感情カテゴリごとに投稿の件数をカウント
    emotion_counts = df['感情'].value_counts()

    # Streamlitでグラフを表示
    st.title("各感情カテゴリの投稿件数")
    st.write("感情カテゴリごとの投稿件数:")
    st.write(emotion_counts)

    # グラフの作成
    fig, ax = plt.subplots(figsize=(10, 6))
    emotion_counts.plot(kind='bar', ax=ax, color=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0'])

    # グラフのラベルとタイトルを設定
    ax.set_ylabel('投稿件数', fontproperties=font_prop)
    ax.set_xlabel('感情カテゴリ', fontproperties=font_prop)
    ax.set_title('各感情カテゴリの投稿件数', fontproperties=font_prop)

    # 凡例を追加
    ax.legend(title="感情カテゴリ", prop=font_prop)

    # Streamlitでグラフを表示
    st.pyplot(fig)