import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager


def display_graph(data):
    # Windowsの日本語フォントを指定（'msgothic.ttc' など）
    font_path = 'msgothic.ttc'  # Windowsの場合

    # フォントプロパティを設定
    font_prop = font_manager.FontProperties(fname=font_path)

    # 日本語フォントをMatplotlibに設定
    plt.rcParams['font.family'] = font_prop.get_name()

    # データの準備


    # データフレームに変換
    df = pd.DataFrame(data, columns=["日時", "役職", "投稿内容", "感情", "非常にネガティブ", "ネガティブ", "ニュートラル", "ポジティブ", "非常にポジティブ"])

    # 感情カテゴリごとに投稿の件数をカウント
    emotion_counts = df['感情'].value_counts()

    # Streamlitでグラフを表示
    st.title("各感情カテゴリの投稿件数")

    # 投稿件数をテキストで表示
    st.write("感情カテゴリごとの投稿件数:")
    st.write(emotion_counts)

    # グラフの作成
    fig, ax = plt.subplots(figsize=(10, 6))

    # 投稿件数を棒グラフとして表示
    emotion_counts.plot(kind='bar', ax=ax, color=['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0'])

    # グラフのラベルとタイトルを設定（日本語フォントを使用）
    ax.set_ylabel('投稿件数', fontproperties=font_prop)
    ax.set_xlabel('感情カテゴリ', fontproperties=font_prop)
    ax.set_title('各感情カテゴリの投稿件数', fontproperties=font_prop)

    # 棒グラフにラベルを追加
    ax.legend(title="感情カテゴリ", prop=font_prop)

    # Streamlitでグラフを表示
    st.pyplot(fig)

def display_graph_stacked(current_data2):
    # 日本語フォントを指定
    font_path = 'C:\\Windows\\Fonts\\msgothic.ttc'  # Windowsの場合
    # LinuxやMacの場合のパスを変更してください

    # フォントプロパティを設定
    font_prop = font_manager.FontProperties(fname=font_path)
    plt.rcParams['font.family'] = font_prop.get_name()

    # データの準備
    # データフレームに変換
    df = pd.DataFrame(current_data2, columns=["日時", "役職", "投稿内容", "感情", "非常にネガティブ", "ネガティブ", "ニュートラル", "ポジティブ", "非常にポジティブ"])

    # インデックスとして時刻を設定
    df.set_index("日時", inplace=True)

    # データを取得
    latest_10_posts = df

    # 感情のカテゴリを指定
    emotion_columns = ["非常にネガティブ", "ネガティブ", "ニュートラル", "ポジティブ", "非常にポジティブ"]
    # 数値データを確認、必要に応じてデータ型を変換
    latest_10_posts[emotion_columns] = latest_10_posts[emotion_columns].apply(pd.to_numeric)
    # Streamlitでグラフを表示
    st.title("最新3件の感情分析結果")

    # グラフの作成
    fig, ax = plt.subplots(figsize=(10, 6))

    # 積み立て棒グラフを作成
    latest_10_posts[emotion_columns].plot(kind='bar', ax=ax, stacked=True, color=['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0'])

    # グラフのラベルとタイトルを設定（日本語フォントを使用）
    ax.set_ylabel('感情の割合', fontproperties=font_prop)
    ax.set_xlabel('投稿', fontproperties=font_prop)
    ax.set_title('感情分析結果', fontproperties=font_prop)

    # 棒グラフにラベルを追加
    ax.legend(title="感情カテゴリ", prop=font_prop)

    # Streamlitでグラフを表示
    st.pyplot(fig)
