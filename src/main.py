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
        
        self.generate_data = []
        self.product_column_nane_list = []

        for c in self.data:
            if c["generate_type"] == "product":
                self.generate_data.append(c["generate_data"])
                self.product_column_nane_list.append(c["column_name"])

    def json_check(data):
        pass

    def make_product_data(self):
        self.df = pd.DataFrame(itertools.product(*self.generate_data), columns=self.product_column_nane_list)

    def make_random_data(self):
        for c in self.data:
            if c["generate_type"] == "random": 
                self.df[c["column_name"]] = random.choices(c["generate_data"], k = len(self.df))

    def output_csv(self, output_path):
        self.df.to_csv(output_path + "/" + self.input_file_name + ".csv", index = False, encoding = "shift-jis")
    
    def get_data(self):
        return self.df

import argparse
parser = argparse.ArgumentParser(description='このプログラムの説明（なくてもよい）')
parser.add_argument('-json_file', "-j", help='この引数の説明（なくてもよい）')
parser.add_argument('-output_path', "-o", help='この引数の説明（なくてもよい）')
args = parser.parse_args()    # 4. 引数を解析

def main():
    json_file = args.json_file
    output_path = args.output_path

    print(json_file, output_path)
    
    dummydata_generator = DummyDataGenerator(json_file)
    dummydata_generator.make_product_data()
    dummydata_generator.make_random_data()
    dummydata_generator.output_csv(output_path)


if __name__ == "__main__" :
    main()
