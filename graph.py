import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams

# フォントファイルのパスを指定
font_path = "assets/fonts/ipaexg.ttf"
rcParams['font.family'] = font_path
# フォント設定（DejaVu Sansを使用）
#plt.rcParams['font.family'] = 'ipaexg.ttf'

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

    # 投稿件数を棒グラフとして表示
    emotion_counts.plot(kind='bar', ax=ax, color=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0'])

    # グラフのラベルとタイトルを設定（DejaVu Sansを使用）
    ax.set_ylabel('投稿件数')
    ax.set_xlabel('感情カテゴリ')
    ax.set_title('各感情カテゴリの投稿件数')

    # 棒グラフにラベルを追加
    ax.legend(title="感情カテゴリ")

    # Streamlitでグラフを表示
    st.pyplot(fig)

def display_graph_stacked(current_data2):
    # データフレームに変換
    df = pd.DataFrame(current_data2, columns=["日時", "役職", "投稿内容", "感情", "非常にネガティブ", "ネガティブ", "ニュートラル", "ポジティブ", "非常にポジティブ"])

    # インデックスとして時刻を設定
    df.set_index("日時", inplace=True)

    # 感情のカテゴリを指定
    emotion_columns = ["非常にネガティブ", "ネガティブ", "ニュートラル", "ポジティブ", "非常にポジティブ"]
    df[emotion_columns] = df[emotion_columns].apply(pd.to_numeric, errors='coerce').fillna(0)

    # Streamlitでグラフを表示
    st.title("最新の感情分析結果")

    # グラフの作成
    fig, ax = plt.subplots(figsize=(10, 6))

    # 積み立て棒グラフを作成
    df[emotion_columns].plot(kind='bar', ax=ax, stacked=True, color=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0'])

    # グラフのラベルとタイトルを設定（DejaVu Sansを使用）
    ax.set_ylabel('感情の割合')
    ax.set_xlabel('投稿')
    ax.set_title('感情分析結果')

    # 凡例を追加
    ax.legend(title="感情カテゴリ")

    # Streamlitでグラフを表示
    st.pyplot(fig)