# Souichirou_Ishikawa_Portfolio
過去作った資産を並べます

<hr />

## 勉強のために行った　かんたんな分析
### 1.京都府農業産出額 の分析

* データについて
  * [利用したデータ](https://github.com/koreisami/ishikawa_Portfolio/blob/main/data/origin/kyoto_farm_product.md)
* 前処理 : 分析しやすいようにデータを加工する
  * [前処理説明](https://github.com/koreisami/ishikawa_Portfolio/blob/main/data/preprocess.md)
  * [前処理のプログラムコード](https://github.com/koreisami/ishikawa_Portfolio/blob/main/data/pre_process.py)
  * Python (pandas) で実施している
  * 欠損値の補間方法には課題がある
* グラフ描画 : 各品目の傾向をグラフ描画で掴む
  * [グラフ描画の説明](https://github.com/koreisami/ishikawa_Portfolio/blob/main/simple_ts/simple_plot.md)
  * [グラフ描画のプログラムコード](https://github.com/koreisami/ishikawa_Portfolio/blob/main/simple_ts/simple_plot.py)

### 2. 京都府農業産出額 の減少要因の分析
* グラフ上は京都府農業産出額が下降傾向にある
* この下降傾向の原因を分析する
* 以下の考察に記載
  * [考察](https://github.com/koreisami/ishikawa_Portfolio/blob/main/%E8%80%83%E5%AF%9F/think_1st.md)

### 98. 権利関係
データを各県のデータカタログより取得しています<br>
京都府/静岡県関連のデータは[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.ja)に準じており、本サイトではそのデータを分析に使用するため、編集を行っています<br>
静岡県関連のデータは


### 99. 実行環境
* 私の実行環境におけるインストールパッケージリスト
  * [requirements.txt](https://github.com/koreisami/ishikawa_Portfolio/blob/main/requirement/requirements.txt)
