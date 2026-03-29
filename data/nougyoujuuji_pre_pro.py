# 農業従事者データ前処理
# import library
import pandas as pd
import os

# Datafile 
target_data_file = ".//origin//nougyoujuuji_orig.csv"

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
    "gender", # 性別
    "item", # 項目
    "value", # 数値 
    "unit" # 単位
]

# 必要な列だけに絞り込み
need_col = [
    "west_calender_yr",
    "region_code",
    "gender",
    "item",
    "value"
]
target_data_selected = target_data_orig.reindex(need_col,axis=1)

# 年書式の変更
target_data_selected.loc[:,"west_calender_yr"] = target_data_selected.loc[:,"west_calender_yr"].str.removesuffix("年")
target_data_selected["west_calender_yr"] = target_data_selected["west_calender_yr"].astype(int)

# Salesの末尾の余分な半角スペースの削除
target_data_selected.loc[:,"value"] = target_data_selected.loc[:,"value"].str.removesuffix(' ')

# 京都府全体のみで抽出
target_data_selected["region_code"] = target_data_selected["region_code"].astype(int)

# 府全体のコードは26000
query_str = "region_code == 26000"
target_data_selected = target_data_selected.query(query_str)
target_data_selected = target_data_selected.drop("region_code",axis=1)

# 項目と性別を結合
target_data_selected.loc[:,"item_gender"] = target_data_selected.loc[:,"item"] + "_" + target_data_selected.loc[:,"gender"]
target_data_selected = target_data_selected.drop("item",axis=1)
target_data_selected = target_data_selected.drop("gender",axis=1)

target_data_selected_wide = target_data_selected.pivot(columns="item_gender",index="west_calender_yr",values="value")

# 分離している総数を足し算
# 足し算をする前に　整数にしておかないといけない
target_data_selected_wide = target_data_selected_wide.fillna(0)
target_data_selected_wide["15歳以上世帯員総数_全体"] = target_data_selected_wide["15歳以上世帯員総数_全体"].astype(int)
target_data_selected_wide["16歳以上総数_全体"] = target_data_selected_wide["16歳以上総数_全体"].astype(int)
target_data_selected_wide_conbine = target_data_selected_wide["15歳以上世帯員総数_全体"] + target_data_selected_wide["16歳以上総数_全体"]

# CSV出力
target_data_selected_wide_conbine.to_csv("補間前.csv")

# 1年ごとの行を作成する
target_year = range(1990,2021)
target_data_selected_wide_conbine_w_hokan = target_data_selected_wide_conbine.reindex(index=target_year)
# 線形補間
target_data_selected_wide_conbine_w_hokan.interpolate(inplace=True)

target_data_selected_wide_conbine_w_hokan.to_csv("PreProcess_Kyoto_nougyoujuujisha_Tsdata_1990_2020.csv")

