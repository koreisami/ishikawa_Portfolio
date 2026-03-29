# 京都府農業生産高と従事者との関係を分析するコード

# import library
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib_fontja
from sklearn import linear_model

# Data file
Aggri_data_file = "..//data//PreProcess_Kyoto_Agri_Tsdata_1987_2019.csv"
Jujisha_data_file = "..//data//PreProcess_Kyoto_nougyoujuujisha_Tsdata_1990_2020.csv"

# 生産高ファイルの読み込み
Aggri_data = pd.read_csv(Aggri_data_file,index_col=0)
# 従事者ファイルの読み込み
Jujisha_data = pd.read_csv(Jujisha_data_file,index_col=0)

# 範囲限定
# 各時系列データの共通部分を使用する
ts_range = range(1990,2020)

# 農業産出額のみ選び、更に共通部分のみ利用する
Aggri_data_selected = Aggri_data["農業産出額_New"].reindex(ts_range,axis=0)
Jujisha_data_selected = Jujisha_data.reindex(ts_range,axis=0)

# 横方向に結合
conbine_agri_Jujisha = pd.concat([Aggri_data_selected,Jujisha_data_selected],axis=1)

# カラムの名称変更
conbine_agri_Jujisha.columns = [
    "農業産出額(百万円)",
    "農業従事者(人)"
]

conbine_agri_Jujisha.to_csv("conbine_Agri_Jujisha_data.csv")
# 散布図の作成
conbine_agri_Jujisha.plot.scatter(x="農業従事者(人)",
                                  y="農業産出額(百万円)",                                 
                                  title="散布図（産出額、従事者)")


# 相関係数の計算
conbine_agri_Jujisha_cor = conbine_agri_Jujisha.corr()
print("相関行列: {}".format(conbine_agri_Jujisha_cor))

# 単回帰線形モデルの形成
# 被説明変数：農業産出額(百万円)
# 説明変数：農業従事者(人)
# 切片あり

# 線型回帰モデルインスタンスの作成(切片あり)
lreg_model = linear_model.LinearRegression(fit_intercept=True)

# 説明変数 
explain_val = conbine_agri_Jujisha.loc[:,["農業従事者(人)"]].to_numpy().reshape(-1,1)
# 被説明変数
explained_val = conbine_agri_Jujisha.loc[:,["農業産出額(百万円)"]].to_numpy().reshape(-1,1)

# 単回帰実行（学習）
lreg_model.fit(explain_val,explained_val)

# 回帰係数の表示
print("回帰係数 : {}".format(lreg_model.coef_))

# 切片の表示
print("切片 : {}".format(lreg_model.intercept_))

# 重相関係数
print("重相関係数 : {}".format(lreg_model.score(explain_val,explained_val)))


plt.savefig("散布図_算出_従事者.png")