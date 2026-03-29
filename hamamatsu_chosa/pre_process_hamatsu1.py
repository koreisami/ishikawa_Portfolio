## 浜松アンケートデータを整理する
## まずはカラム名などの整理

import pandas as pd

# データ本体の取得
# データ本体ファイル名
data_file_name = ".//data//221309_hamamatsu_questionnaire_48_0002_utf8.csv"
# データの読み込み
data_file = pd.read_csv(data_file_name,sep='\t',index_col=0)

# テーブル定義の読み込み
# テーブル定義ファイル名
tbl_def_file_name = ".//data//tbl_info.csv"
tbl_def = pd.read_csv(tbl_def_file_name,index_col=0)

# 元データのカラム名を扱いやすくする
data_file.columns = tbl_def.loc[:,"Col_Label"].tolist()
columns_liat = tbl_def.loc[:,"Col_Label"].tolist()

data_file.to_csv("trans_col_data.csv")

def create_dimension(coldata:pd.Series) -> bool:
    not_dup_coldata = coldata.drop_duplicates()
    outfile = ".//dimension//dim_tbl_{}.tsv".format(coldata.name)
    sort_key = coldata.name

    not_dup_coldata = not_dup_coldata.reset_index()
    not_dup_coldata = not_dup_coldata.drop("No.",axis=1)
    not_dup_coldata = not_dup_coldata.sort_values(by=sort_key)
    not_dup_coldata = not_dup_coldata.reset_index()
    not_dup_coldata = not_dup_coldata.drop("index",axis=1)
    not_dup_coldata.to_csv(outfile,sep="\t")
    return True

data_file.apply(create_dimension)

for col_arg in columns_liat:
    dim_file = ".//dimension//dim_tbl_{}.tsv".format(col_arg)
    new_colname = "new_{}".format(col_arg)
    new_col = [new_colname,col_arg]
    dim_data = pd.read_csv(dim_file,sep="\t")
    dim_data.columns = new_col
    dim_data.loc[:,new_colname] = dim_data.loc[:,new_colname].astype(int)
    data_file = pd.merge(data_file,dim_data,on=col_arg,how="left")
    data_file = data_file.drop(col_arg,axis=1)

data_file.to_csv("normalize_fact_tbl.tsv",sep="\t")