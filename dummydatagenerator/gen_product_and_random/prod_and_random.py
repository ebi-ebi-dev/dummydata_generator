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
        for c in self.data:
            self.column_name_list.append(c["column_name"])
        
        self.df_set = {}

        for c in self.data:
            # 以下の場合、左辺が不成立の場合、右辺は評価されないので、キーが入っているかの評価は必ず必要。
            # if comp1 and comp2
            if "generate_type" in c and c["column_name"] not in self.df_set: 
                self.df_set[c["column_name"]] = pd.DataFrame()
            elif "linked_cname" in c and c["linked_cname"] not in self.df_set: # linkのカラムがlinkedされるカラムよりも先にjsonに記述されている場合
                self.df_set[c["linked_cname"]] = pd.DataFrame()
            if "generate_type" in c and c["generate_type"] == "product":
                self.df_set[c["column_name"]][c["column_name"]] = c["generate_data"]
            if "linked_cname" in c:
                self.df_set[c["linked_cname"]][c["column_name"]] = c["generate_data"]

    def json_check(data):
        # 同じカラム名はあってはだめ。
        # 
        pass

    def make_product_data(self):

        def recursive_merge(df_list):
            print(len(df_list))
            if len(df_list) <=2:
                print(df_list[0]) 
                print(df_list[1]) 
                return pd.merge(df_list[0], df_list[1], how = "cross")
            else:
                return pd.merge(recursive_merge(df_list[:len(df_list)-1]), df_list[len(df_list)-1], how="cross")

        df_list = []
        for v in self.df_set.values(): 
            df_list.append(v)
        self.df = recursive_merge(df_list)
        

    def make_random_data(self):
        for c in self.data:
            if "generate_type" in c and c["generate_type"] == "random": 
                self.df[c["column_name"]] = random.choices(c["generate_data"], k = len(self.df))

    def output_csv(self, output_path):
        self.df.to_csv(output_path + "/" + self.input_file_name + ".csv", index = False, encoding = "shift-jis")
    
    def get_data(self):
        return self.df