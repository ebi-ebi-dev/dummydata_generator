import prod_and_random
import create
import make_trend
import io

import datetime
def test_create():
    create_data = create.CreateData()
    # create_data.create_date("date", "product","2023/03/12", "2023/03/15", 1)
    # print(create_data.data)
    # create_data.create_link_date("enddate", "date", "2023/02/01", "2023/02/11", 1)
    # create_data.create_datetime("datetime", "product","2023/02/25 00:00:00", "2023/02/25 10:00:00", 60 * 60)
    # create_data.create_link_datetime("enddatetime", "datetime", "2023/02/25 00:00:00", "2023/02/25 10:00:00", 1, 59, 60*60)
    # create_data.create_list("code", "random", [
    #     "a",
    #     "b",
    #     "c"
    # ])
    # create_data.create_link_list("value", "code", [
    #   "A",
    #   "B",
    #   "C"
    # ])
    # create_data.create_list("code2", "product", [
    #     "11",
    #     "22",
    #     "33"
    # ])
    # create_data.create_link_list("value2", "code2", [
    #     "one",
    #     "two",
    #     "three"
    # ])
    create_data.create_amount("number", "random", float(-10), float(10), float(0.5))
    # create_data.output_json("./output/input_sample_generated.json")
    print(create_data.data)

def test_prod_and_random():
    # json_file = "./input/input_sample_noProduct.json"
    # json_file = "./input/input_sample_noRandom.json"
    json_file = "./input/input_sample4.json"
    # json_file = "./output/input_sample_generated.json"
    output_path = "./output"

    # print(json_file, output_path)
    
    dummydata_generator = prod_and_random.DummyDataGenerator()
    dummydata_generator.read_from_jsonpath(json_file)
    dummydata_generator.json_check()
    dummydata_generator.prepare_prod_and_random()
    dummydata_generator.make_product_data()
    dummydata_generator.make_random_data()
    # dummydata_generator.output_csv(output_path)
    print(dummydata_generator.df)


def test_make_trend():
    import csv
    import pprint

    # csv_file= "./output/定数_float.csv"
    csv_file= "./output/定数.csv"
    with open(csv_file, encoding = "utf-8") as f:
        csv_test = f.read()
    
    maketrend = make_trend.makeTrend()
    maketrend.read_from_csvtext(csv_test)
    maketrend.trend_x("日付", "数値", 1/2)
    maketrend.trend_sinx("日付", "数値", 2, 0.5)
    maketrend.output_csv("./output/定数_changed_float.csv")


if __name__ == "__main__" :
    test_create()
    # test_prod_and_random()
    # test_make_trend()