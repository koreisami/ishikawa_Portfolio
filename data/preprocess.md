# 前処理
## やっていること

* wide 型テーブルへの変換
  * いわゆる縦軸時刻、横軸品目、中の値は売上値の表
* 単位の統一
  * 売上に関して　百万、千万、億が混ざっているため、今回は百万に合わせた
* 欠損値補完
  * 今回は一律0 で補完したが、本当はもう少し吟味が必要
* 似たような項目のマージ
  * 種苗・苗木,種苗・苗木その他,種苗･苗木その他　などを一つにまとめた
  * 纏めた列は ***_new とついている

## 前処理前データ
[前処理前データ](https://github.com/koreisami/ishikawa_Portfolio/blob/main/data/origin/target_data.csv)

## 前処理後データ
[前処理後データ](https://github.com/koreisami/ishikawa_Portfolio/blob/main/data/PreProcess_Kyoto_Agri_Tsdata_1987_2019.csv)

  