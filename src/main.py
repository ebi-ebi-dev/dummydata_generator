import pandas as pd
import json
import argparse
import itertools
import random

parser = argparse.ArgumentParser(description='このプログラムの説明（なくてもよい）')
parser.add_argument('-json_file', "-j", help='この引数の説明（なくてもよい）')
parser.add_argument('-output_path', "-o", help='この引数の説明（なくてもよい）')
args = parser.parse_args()    # 4. 引数を解析

def json_check(data):
    pass

def make_init_data(data):
    column_name_list = []
    
    for c in data:
        column_name_list.append(c["column_name"])

    generate_data = []
    product_column_nane_list = []
    for c in data:
        if c["generate_type"] == "product":
            generate_data.append(c["generate_data"])
            product_column_nane_list.append(c["column_name"])

    df = pd.DataFrame(itertools.product(*generate_data), columns=product_column_nane_list)

    for c in data:
        if c["generate_type"] == "random": 
            df[c["column_name"]] = random.choices(c["generate_data"], k = len(df))
    
    print(df)

def make_product_data(data):
    pass


def make_random_data(data):
    pass

def main():
    json_file = args.json_file
    output_path = args.output_path

    print(json_file, output_path)

    with open(json_file, "r") as f:
        data = json.load(f)
    
    json_check(data)
    make_init_data(data)
    make_product_data(data)
    make_random_data(data)


if __name__ == "__main__" :
    main()
