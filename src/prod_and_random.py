import pandas as pd
import json
import itertools
import random

class DummyDataGenerator:

    def __init__(self, json_path): 
        self.input_file_name = json_path.split("/")[-1].split(".")[0]

        with open(json_path, "r") as f:
            self.data = json.load(f)
        
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

    def json_check(data):
        # 同じカラム名はあってはだめ。
        # 
        pass

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