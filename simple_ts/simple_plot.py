import pandas as pd
import matplotlib.pyplot as plt
import matplotlib_fontja

target_data_file = "..//data//PreProcess_Kyoto_Agri_Tsdata_1987_2019.csv"

target_data = pd.read_csv(target_data_file,index_col=0)

# 農作物品目
Aggri_Items=[
    "いも類",
    "その他畜産物",
    "乳用牛",
    "加工農産物",
    "工芸農作物",
    "果実",
    "生産農業所得",
    "畜産計",
    "米",
    "耕種計",
    "肉用牛",
    "花き",
    "豚",
    "野菜",
    "雑穀・豆類",
    "養蚕",
    "鶏",
    "麦類",
    "種苗苗木_new",
    "農業産出額_New"
]

# 移動平均付きプロット
def plot_aggri_sale_with_moving_average(df:pd.DataFrame, 
                                        item:str,
                                        w:int) -> bool:
    # 移動平均の計算
    df.loc[:,"trend_{}".format(item)] = df.loc[:,item].rolling(window=w,center=True).mean()
    df[[item,"trend_{}".format(item)]].plot(figsize=(10,6))
    plt.title("Sales(Kyoto Agriculture)_{}".format(item))
    plt.savefig("plot{}.png".format(item))
    return True

for item_arg in Aggri_Items:
    plot_aggri_sale_with_moving_average(target_data,item_arg,5)