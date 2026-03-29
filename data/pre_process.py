
# import library
import pandas as pd
import os

# Datafile 
target_data_file = ".//origin//target_data.csv"

# read file
if os.path.isfile(target_data_file):
    target_data_orig = pd.read_csv(target_data_file)
else: 
    print("File Not Exist")
    os._exit(-1)

# カラムの付替え
target_data_orig.columns = [
    "time_code", # 時間軸コード
    "west_calender_yr", # 西暦
    "japan_yr", # 和暦
    "region_code", # 地域コード 
    "region", # 地域
    "item", # 品目
    "Sales", # 売上値
    "Unit" # 売上単位
]

# 必要な列だけに絞り込み
need_col = [
    "west_calender_yr",
    "item",
    "Sales",
    "Unit"
]
target_data_selected = target_data_orig.reindex(need_col,axis=1)

# 年初式の変更
target_data_selected.loc[:,"west_calender_yr"] = target_data_selected.loc[:,"west_calender_yr"].str.removesuffix("年")
target_data_selected["west_calender_yr"] = target_data_selected["west_calender_yr"].astype(int)

# Salesの末尾の余分な半角スペースの削除
target_data_selected.loc[:,"Sales"] = target_data_selected.loc[:,"Sales"].str.removesuffix(' ')
# 単位合わせ　(すべての売上を百万円単位とする)
# 欠損値はひとまず0埋めとしている
def Match_the_unit(x:pd.Series) -> pd.Series:
    # 文字列判別
    target = x["Sales"]
    ret = x
    if(target.isdigit()):
        if(x["Unit"] == "千万円"):
            ret["Sales"] = str(x["Sales"]) + '0'
        elif(x["Unit"] == "億円"):
            ret["Sales"] = str(x["Sales"]) + '00'
    else: # 欠損値、変な文字列が入っている場合
        ret["Sales"] = '0'
    return ret
target_data_selected = target_data_selected.apply(Match_the_unit,axis=1)

# 単位を統一したので、単位列削除
target_data_selected = target_data_selected.drop("Unit",axis=1)
target_data_selected["Sales"] = target_data_selected["Sales"].astype(int)

# wide 型へ変換
target_data_selected_wide = target_data_selected.pivot(index="west_calender_yr",
                                                       columns="item",
                                                       values="Sales")
target_data_selected_wide = target_data_selected_wide.astype("Int64")

# 0を欠損値として補完
# これは　後段で　種苗・苗木,種苗・苗木その他,種苗･苗木その他　などを一つに纏めるため
target_data_selected_wide = target_data_selected_wide.fillna(0)

# 時期によって品目名が変わったものの統一
# 種苗・苗木,種苗・苗木その他,種苗･苗木その他, -> これを　種苗苗木_new とする
target_data_selected_wide.loc[:,"種苗苗木_new"] = target_data_selected_wide.loc[:,"種苗・苗木"] + target_data_selected_wide.loc[:,"種苗・苗木その他"] + target_data_selected_wide.loc[:,"種苗･苗木その他"]
target_data_selected_wide = target_data_selected_wide.drop("種苗・苗木",axis=1)
target_data_selected_wide = target_data_selected_wide.drop("種苗・苗木その他",axis=1)
target_data_selected_wide = target_data_selected_wide.drop("種苗･苗木その他",axis=1)

# 農業産出額,農業粗生産額 -> 農業産出額_Newとする
target_data_selected_wide.loc[:,"農業産出額_New"] = target_data_selected_wide.loc[:,"農業産出額"] + target_data_selected_wide.loc[:,"農業粗生産額"]
target_data_selected_wide = target_data_selected_wide.drop("農業産出額",axis=1)
target_data_selected_wide = target_data_selected_wide.drop("農業粗生産額",axis=1)

target_data_selected_wide.to_csv("PreProcess_Kyoto_Agri_Tsdata_1987_2019.csv")
