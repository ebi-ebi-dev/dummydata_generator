import pandas as pd
import json
import itertools
import random


error_templete = """
Set following json format
{
    "column_name": "code",
    "generate_type": "random",
    "generate_data": [
        "a",
        "b",
        "c"
    ]
},
{
    "column_name": "value",
    "linked_cname": "code",
    "generate_data": [
        "A",
        "B",
        "C"
    ]
}
"""

class DummyDataGenerator:

    def __init__(self, json_path): 
        self.input_file_name = json_path.split("/")[-1].split(".")[0]

        with open(json_path, "r", encoding="utf-8_sig") as f:
            self.data = json.load(f)
    
    def json_check(self):
        # 特定のカラムがないとだめ
        # 必ずキーの数は3つで、以下2パターンのいずれか
        # ・["column_name": str, "generate_type": "product" or "random", "generate_data": list]
        # ・["column_name": str, "linked_cname": str, "generate_data": list]
        
        for c, idx in zip(self.data, range(len(self.data))):
            error_form = ""
            for key, value in c.items(): 
                error_form = error_form + f"{key} : {value}\n"
            if len(c.keys()) == 3:
                if ("column_name" in c and "generate_type" in c and "generate_data" in c) or ("column_name" in c and "linked_cname" in c and "generate_data" in c):
                    pass
                else:
                    raise Exception(
                        "No. {idx} is error format: \n".format(idx = idx + 1)
                        + error_form
                        + error_templete
                    )
            else:
                raise Exception(
                    "No. {idx} is error format: \n".format(idx = idx + 1)
                    + error_form
                    + error_templete
                )

        # 同じカラム名はあってはだめ。
        column_name_list = []
        for c, idx in zip(self.data, range(len(self.data))):
            if c["column_name"] in column_name_list:
                error_msg = "No. {idx} '{cname}' is already specified at No. {idx_ex} data. ".format(idx = idx + 1, cname = c["column_name"], idx_ex = column_name_list.index(c["column_name"]) + 1)
                print(error_msg)
                raise Exception(error_msg)
            else:
                column_name_list.append(c["column_name"])
        
        # generate_typeはproductかrandomでないとだめ
        for c, idx in zip(self.data, range(len(self.data))):
            if("generate_type" in c):
                if "product" == c["generate_type"] or "random" == c["generate_type"]:
                    pass
                else:
                    raise Exception(
                        "No. {idx} generate_type '{gtype}' must be 'product' or 'random'. ".format(idx = idx + 1, gtype = c["generate_type"])
                    )
        
        # linked_cnameは存在しているカラムを指定しないとだめ
        origin_column_name_list = []
        for c in self.data:
            if("generate_type" in c):
                origin_column_name_list.append(c["column_name"])
        for c, idx in zip(self.data, range(len(self.data))):
            if("linked_cname" in c):
                if c["linked_cname"] in origin_column_name_list:
                    pass
                else:
                    raise Exception(
                        "No. {idx} linked_cname '{cname}' is not exist. ".format(idx = idx + 1, cname = c["linked_cname"])
                    )
        # originカラムとlinkカラムのデータサイズは同じにしないとだめ
        origin_column_datasize = {}
        for c in self.data:
            if("generate_type" in c):
                origin_column_datasize[c["column_name"]] = len(c["generate_data"])
        for c, idx in zip(self.data, range(len(self.data))):
            if("linked_cname" in c):
                if origin_column_datasize[c["linked_cname"]] == len(c["generate_data"]):
                    pass
                else:
                    raise Exception(
                        "No. {idx} datasize '{cname}: {size}' is not match linked datasize '{cname_l}: {size_l}'. ".format(
                            idx = idx + 1, cname = c["column_name"], size = len(c["generate_data"]), cname_l = c["linked_cname"], size_l = origin_column_datasize[c["linked_cname"]]
                        )
                    )

    def prepare_prod_and_random(self):    
        self.column_name_list = []
        prod_column_list = []
        rand_column_list = []
        for c in self.data:
            self.column_name_list.append(c["column_name"])
            if "generate_type" in c and c["generate_type"] == "product": prod_column_list.append(c["column_name"])
            if "generate_type" in c and c["generate_type"] == "random": rand_column_list.append(c["column_name"])
        
        self.prod_df_set = {}
        self.rand_df_set = {}

        for c in self.data:
            # DataFrameの箱を作る。
            if "generate_type" in c:
                if c["generate_type"] == "product":
                    if c["column_name"] not in self.prod_df_set: 
                        self.prod_df_set[c["column_name"]] = pd.DataFrame()
                elif c["generate_type"] == "random":
                    if c["column_name"] not in self.rand_df_set: 
                        self.rand_df_set[c["column_name"]] = pd.DataFrame()
            elif "linked_cname" in c: # linkのカラムがlinkedされるカラムよりも先にjsonに記述されている場合
                if c["linked_cname"] in prod_column_list:
                    if c["linked_cname"] not in self.prod_df_set: 
                        self.prod_df_set[c["linked_cname"]] = pd.DataFrame()
                elif c["linked_cname"] in rand_column_list:
                    if c["linked_cname"] not in self.rand_df_set:
                        self.rand_df_set[c["linked_cname"]] = pd.DataFrame()
            # データを格納していく
            if "generate_type" in c:
                if c["generate_type"] == "product":
                    self.prod_df_set[c["column_name"]][c["column_name"]] = c["generate_data"]
                elif c["generate_type"] == "random":
                    # print(c["column_name"], c["generate_data"])
                    self.rand_df_set[c["column_name"]][c["column_name"]] = c["generate_data"]
            if "linked_cname" in c:
                if c["linked_cname"] in prod_column_list:
                    self.prod_df_set[c["linked_cname"]][c["column_name"]] = c["generate_data"]
                elif c["linked_cname"] in rand_column_list:
                    self.rand_df_set[c["linked_cname"]][c["column_name"]] = c["generate_data"]

    def make_product_data(self):

        def recursive_merge(df_list):
            if len(df_list) <=2:
                return pd.merge(df_list[0], df_list[1], how = "cross")
            else:
                return pd.merge(recursive_merge(df_list[:len(df_list)-1]), df_list[len(df_list)-1], how="cross")

        df_list = []
        for v in self.prod_df_set.values(): 
            df_list.append(v)
        self.df = recursive_merge(df_list)

    def make_random_data(self):
        for v in self.rand_df_set.values():
            tmp = random.choices(v.values.tolist(), k = len(self.df))
            data_list = [list(x) for x in zip(*tmp)]
            for c, i in zip(v.columns, range(len(v.columns))):
                self.df[c] = data_list[i]

        # for c in self.data:
        #     if "generate_type" in c and c["generate_type"] == "random": 
        #         self.df[c["column_name"]] = random.choices(c["generate_data"], k = len(self.df))

    def output_csv(self, output_path):
        self.df.to_csv(output_path + "/" + self.input_file_name + ".csv", index = False, encoding = "shift-jis")
    
    def get_data(self):
        return self.df