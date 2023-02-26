import pandas as pd
import json
import itertools
import random
import datetime

class CreateData:

    def __init__(self): 
        self.data = []

    def create_date(self, cname, generate_type, start, end, step = 1):
        start = datetime.datetime.strptime(start, "%Y/%m/%d").date()
        end = datetime.datetime.strptime(end, "%Y/%m/%d").date()
        days_num = (end - start).days
        datalist = [(start + datetime.timedelta(days=x)).strftime("%Y/%m/%d") for x in range(0, days_num, step)]
        self.data.append(
            {
                "column_name" : cname,
                "generate_type" : generate_type,
                "generate_data" : datalist
            }
        )
    
    def create_link_date(self, cname, linked_cname, min, max):
        for d in self.data:
            if d["column_name"] == linked_cname:
                linked_data = d["generate_data"]
        
        random_add = lambda tmp, min, max: datetime.datetime.strptime(tmp, "%Y/%m/%d").date() + datetime.timedelta(days=random.randint(min, max))
        datalist = [ random_add(tmp_date, min, max).strftime("%Y/%m/%d") for tmp_date in linked_data]
        self.data.append(
            {
                "column_name" : cname,
                "linked_cname" : linked_cname,
                "generate_data" : datalist
            }
        )
    
    def create_datetime(self, cname, generate_type, start, end, step = 1):
        start = datetime.datetime.strptime(start, "%Y/%m/%d %H:%M:%S")
        end = datetime.datetime.strptime(end, "%Y/%m/%d %H:%M:%S")
        days_num = (end - start).seconds
        datalist = [(start + datetime.timedelta(seconds=x)).strftime("%Y/%m/%d %H:%M:%S") for x in range(0, days_num, step)]
        self.data.append(
            {
                "column_name" : cname,
                "generate_type" : generate_type,
                "generate_data" : datalist
            }
        )
    
    def create_link_datetime(self, cname, linked_cname, min, max):
        for d in self.data:
            if d["column_name"] == linked_cname:
                linked_data = d["generate_data"]
        
        random_add = lambda tmp, min, max: datetime.datetime.strptime(tmp, "%Y/%m/%d %H:%M:%S") + datetime.timedelta(seconds=random.randint(min, max))
        datalist = [ random_add(tmp_datetime, min, max).strftime("%Y/%m/%d %H:%M:%S") for tmp_datetime in linked_data]
        self.data.append(
            {
                "column_name" : cname,
                "linked_cname" : linked_cname,
                "generate_data" : datalist
            }
        )
    
    def create_amount(self, cname, generate_type, start, end, step = 1):
        datalist = [x for x in range(start, end, step)]
        self.data.append(
            {
                "column_name" : cname,
                "generate_type" : generate_type,
                "generate_data" : datalist
            }
        )
    
    def create_list(self, cname, generate_type, list):
        self.data.append(
            {
                "column_name" : cname,
                "generate_type" : generate_type,
                "generate_data" : list
            }
        )
    
    def create_link_list(self, cname, linked_cname, list):
        self.data.append(
            {
                "column_name" : cname,
                "linked_cname" : linked_cname,
                "generate_data" : list
            }
        )
    
    def output_json(self, output_file):
        with open(output_file, 'w') as f:
            json.dump(self.data, f, ensure_ascii=False, indent=2)