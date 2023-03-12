import pandas as pd
import json
import itertools
import random
import datetime
import numpy as np

class CreateData:

    def __init__(self): 
        self.data = {}

    def create_date(self, cname:str, generate_type:str, start:str, end:str, step:int):
        start = datetime.datetime.strptime(start, "%Y/%m/%d").date()
        end = datetime.datetime.strptime(end, "%Y/%m/%d").date()
        days_num = (end - start).days
        datalist = [(start + datetime.timedelta(days=x)).strftime("%Y/%m/%d") for x in range(0, days_num, step)]
        self.data = {
            "column_name" : cname,
            "generate_type" : generate_type,
            "generate_data" : datalist
        }
    
    def create_link_date(self, cname:str, linked_cname:str, start:str, end:str, step:int, min:int, max:int):
        start = datetime.datetime.strptime(start, "%Y/%m/%d").date()
        end = datetime.datetime.strptime(end, "%Y/%m/%d").date()
        days_num = (end - start).days

        origin_datalist = [(start + datetime.timedelta(days=x)).strftime("%Y/%m/%d") for x in range(0, days_num, step)]
        
        random_add = lambda tmp, min, max: datetime.datetime.strptime(tmp, "%Y/%m/%d").date() + datetime.timedelta(days=random.randint(min, max))
        datalist = [ random_add(tmp_date, min, max).strftime("%Y/%m/%d") for tmp_date in origin_datalist]
        self.data = {
            "column_name" : cname,
            "linked_cname" : linked_cname,
            "generate_data" : datalist
        }
    
    def create_datetime(self, cname:str, generate_type:str, start:str, end:str, step:int):
        start = datetime.datetime.strptime(start, "%Y/%m/%d %H:%M:%S")
        end = datetime.datetime.strptime(end, "%Y/%m/%d %H:%M:%S")
        seconds_num = int((end - start).total_seconds())
        print(end - start, seconds_num)
        datalist = [(start + datetime.timedelta(seconds=x)).strftime("%Y/%m/%d %H:%M:%S") for x in range(0, seconds_num, step)]
        self.data = {
            "column_name" : cname,
            "generate_type" : generate_type,
            "generate_data" : datalist
        }
    
    def create_link_datetime(self, cname:str, linked_cname:str, start:str, end:str, step:int, min:int, max:int):
        start = datetime.datetime.strptime(start, "%Y/%m/%d %H:%M:%S")
        end = datetime.datetime.strptime(end, "%Y/%m/%d %H:%M:%S")
        seconds_num = int((end - start).total_seconds())
        origin_datalist = [(start + datetime.timedelta(seconds=x)).strftime("%Y/%m/%d %H:%M:%S") for x in range(0, seconds_num, step)]

        
        random_add = lambda tmp, min, max: datetime.datetime.strptime(tmp, "%Y/%m/%d %H:%M:%S") + datetime.timedelta(seconds=random.randint(min, max))
        datalist = [ random_add(tmp_datetime, min, max).strftime("%Y/%m/%d %H:%M:%S") for tmp_datetime in origin_datalist]
        self.data = {
            "column_name" : cname,
            "linked_cname" : linked_cname,
            "generate_data" : datalist
        }
    
    def create_amount(self, cname:str, generate_type:str, min:float, max:float, step:float):
        datalist = [x for x in np.arange(min, max, step)]
        self.data = {
            "column_name" : cname,
            "generate_type" : generate_type,
            "generate_data" : datalist
        }
    
    def create_link_amount(self, cname:str, generate_type:str, min: float, max: float, step : float):
        datalist = [x for x in np.arange(min, max, step)]
        self.data = {
            "column_name" : cname,
            "linked_cname" : generate_type,
            "generate_data" : datalist
        }

    
    def create_list(self, cname:str, generate_type:str, list: list):
        self.data = {
            "column_name" : cname,
            "generate_type" : generate_type,
            "generate_data" : list
        }

    
    def create_link_list(self, cname:str, linked_cname:str, list: list):
        self.data = {
            "column_name" : cname,
            "linked_cname" : linked_cname,
            "generate_data" : list
        }

    
    def output_json(self, output_file):
        with open(output_file, 'w') as f:
            json.dump(self.data, f, ensure_ascii=False, indent=2)