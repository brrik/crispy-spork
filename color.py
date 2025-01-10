# カスタムスタイル関数
def sentiment_color(val):
    if val == "非常にポジティブ":
        color = "background-color: #98FB98;"  # ライトグリーン
    elif val == "ポジティブ":
        color = "background-color: #D0F0C0;"  # 薄いグリーン
    elif val == "ニュートラル":
        color = "background-color: #F5F5DC;"  # ベージュ
    elif val == "ネガティブ":
        color = "background-color: #FFC0CB;"  # ピンク
    elif val == "非常にネガティブ":
        color = "background-color: #FF6347;"  # トマトレッド
    else:
        color = ""
    return color


