# かんたんな考察
## 可視化を終えて
* わかること
  * やや農業生産額が落ちている
    * 1987年：79124　(百万円)
    * 2019年：66600　(百万円)
  * グラフ
    * ![農業生産額推移](https://github.com/koreisami/ishikawa_Portfolio/blob/main/img/simple_ts/plot_sumof_aggri.png "農業生産額推移")
    * やや移動平均をみても1990 年代に一度上がっているが、やや下降傾向
* ここから考えていきたいこと
  * ではなぜ下降傾向であるのかを探っていく
    * （仮説）単純に作っている人が減ったから？
  * この仮説の検証を行う
    * この仮説の反論は無くはない
      * 人が減っても単価が上がれば、生産額は落ちないのでは？
      * 気象条件が悪ければ生産額は下がるのでは?
      * このあたりを探っていく
## 従事者と生産額との関連分析
* 課題
  * 農業生産額が下降傾向はなぜか？
  * 仮説：農業従事者が減ったから生産額も減る　という仮説の検証
* 実施すること
  * 農業従事者と生産額の相関
  * 生産額を農業従事者で説明するモデルを作成し、農業従事者の増減に対する生産額の増減を見る
* 相関係数
  * 農業従事者と生産額の相関は0.83であった
    * 相関はあるとみなして良い（強いかどうかはちょっと賛否がある）
* 散布図
  * [散布図](https://github.com/koreisami/ishikawa_Portfolio/blob/main/factor_ana/%E6%95%A3%E5%B8%83%E5%9B%B3_%E7%AE%97%E5%87%BA_%E5%BE%93%E4%BA%8B%E8%80%85.png)
  * なんとなく　従事者が増えれば生産額が増えると見える
* 回帰モデル作成
  * 単回帰モデル　農業生産額 = A * 農業従事者 + B というモデルを作成
  * Aは農業従事者が1人増えたら農業生産額はどれだけ増えるか
  * B は考慮が必要だが、農業従事者がいなくても発生する農業生産額
    * 農業従事者が0人ならば 農業生産額は0 が正しいが,,,
* 回帰モデル
  * 結果
    * A = 0.125 (百万/人)
    * B = 62478 (百万)
    * R^2 = 0.687
  * 考察
    * 従事者１人増えると、生産額は　0.125百万　つまり12万5000円が増える
      * 兼業もあるので、だいたいあっているのかな思う
    * R^2 = 0.687 であることから、説明できているといえばいるだが、従事者数だけでは説明できない何かがありそう
    * 他に、被説明変数が額であるため、単価（つまり需要）、気象条件などで説明できる（かも）
    * 気が向いたら 続きをする
* リソース
  * 前処理
    * 農業生産額データの前処理
      * [生産額前処理コード](https://github.com/koreisami/ishikawa_Portfolio/blob/main/data/pre_process.py)
      * 元データ
        * [データソース](https://data.bodik.jp/dataset/260002_tokeisyo0419/resource/cf18f898-37a7-4483-be38-21041ea3802c)
        * [CSVファイル](https://github.com/koreisami/ishikawa_Portfolio/blob/main/data/origin/target_data_orig.csv)
      * 前処理でやってること
        * [前処理説明](https://github.com/koreisami/ishikawa_Portfolio/blob/main/data/preprocess.md)
      * 前処理後データ
        * [前処理後データ](https://github.com/koreisami/ishikawa_Portfolio/blob/main/data/PreProcess_Kyoto_Agri_Tsdata_1987_2019.csv)
    * 農業従事者データの前処理
      * [従事者前処理コード](https://github.com/koreisami/ishikawa_Portfolio/blob/main/data/nougyoujuuji_pre_pro.py)
      * 元データ
        * [データソース](https://data.bodik.jp/dataset/260002_tokeisyo0402)
        * [CSVファイル](https://github.com/koreisami/ishikawa_Portfolio/blob/main/data/origin/nougyoujuuji_orig.csv)
      * 前処理後データ
        * [前処理後データ](https://github.com/koreisami/ishikawa_Portfolio/blob/main/data/nougyoujuuji_pre_pro.py)
  * 本分析
    * 単純可視化
      * 品目ごとの時系列グラフ描画（５年移動平均付き）
      * [グラフ描画コード](https://github.com/koreisami/ishikawa_Portfolio/blob/main/simple_ts/simple_plot.py)
    * 生産額、従事者の関連分析
      * [関連分析コード](https://github.com/koreisami/ishikawa_Portfolio/blob/main/factor_ana/agri_juuji_factar_ana.py)