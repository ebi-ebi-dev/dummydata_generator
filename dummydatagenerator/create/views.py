from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.http import QueryDict

from .forms import *
from django.http.response import JsonResponse
from .create import CreateData

import json

import dummydatagenerator.my_logger as my_logger
mylogger = my_logger.my_logger()
log_format = """[create] {client_ip} > column_name: {column_name}, data_length: {data_length}, sample : {sample}"""
num_pick_up_samples = 10

def create(request):
    if request.method == "POST":
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            dic = dict(QueryDict(request.body, encoding='utf-8'))

            column_name_form = ColumnNameForm(request.POST)
            print(request.POST)
            if "generate" in request.POST:
                print("generate")
            column_name_form
            column_type_form = NormalForm()
            data_type_detail_form = NormalDataTypeForm_Date()

            # 初期値をdicに格納
            if ("column_type" in dic):
                if (dic["column_type"][0] == "normal"):
                    if("data_type" in dic):
                        if (dic["data_type"][0] == "string"):
                            data_type_detail_form = NormalDataTypeForm_Text()
                            if("text" not in dic): dic["text"] = data_type_detail_form["text"].initial
                        if (dic["data_type"][0] == "number"):
                            data_type_detail_form = NormalDataTypeForm_Number()
                            if("number_min" not in dic): dic["number_min"] = data_type_detail_form["number_min"].initial
                            if("number_max" not in dic): dic["number_max"] = data_type_detail_form["number_max"].initial
                            if("number_step" not in dic): dic["number_step"] = data_type_detail_form["number_step"].initial
                        if (dic["data_type"][0] == "date"):
                            data_type_detail_form = NormalDataTypeForm_Date()
                            if("date_min" not in dic): dic["date_min"] = data_type_detail_form["date_min"].initial
                            if("date_max" not in dic): dic["date_max"] = data_type_detail_form["date_max"].initial
                            if("date_step" not in dic): dic["date_step"] = data_type_detail_form["date_step"].initial
                        if (dic["data_type"][0] == "datetime"):
                            data_type_detail_form = NormalDataTypeForm_Datetime()
                            if("datetime_min" not in dic): dic["datetime_min"] = data_type_detail_form["datetime_min"].initial
                            if("datetime_max" not in dic): dic["datetime_max"] = data_type_detail_form["datetime_max"].initial
                            if("datetime_step" not in dic): dic["datetime_step"] = data_type_detail_form["datetime_step"].initial
                if (dic["column_type"][0] == "link"):
                    column_type_form = LinkForm()
                    data_type_detail_form = LinkDataTypeForm_Date()
                    if("data_type" in dic):
                        if (dic["data_type"][0] == "string"):
                            data_type_detail_form = LinkDataTypeForm_Text()
                            if("link_text" not in dic): dic["link_text"] = data_type_detail_form["text"].initial
                        if (dic["data_type"][0] == "number"):
                            data_type_detail_form = LinkDataTypeForm_Number()
                            if("link_number_min" not in dic): dic["link_number_min"] = data_type_detail_form["number_min"].initial
                            if("link_number_max" not in dic): dic["link_number_max"] = data_type_detail_form["number_max"].initial
                            if("link_number_step" not in dic): dic["link_number_step"] = data_type_detail_form["number_step"].initial
                        if (dic["data_type"][0] == "date"):
                            data_type_detail_form = LinkDataTypeForm_Date()
                            if("link_date_min" not in dic): dic["link_date_min"] = data_type_detail_form["date_min"].initial
                            if("link_date_max" not in dic): dic["link_date_max"] = data_type_detail_form["date_max"].initial
                            if("link_date_step" not in dic): dic["link_date_step"] = data_type_detail_form["date_step"].initial
                        if (dic["data_type"][0] == "datetime"):
                            data_type_detail_form = LinkDataTypeForm_Datetime()
                            if("link_datetime_min" not in dic): dic["link_datetime_min"] = data_type_detail_form["datetime_min"].initial
                            if("link_datetime_max" not in dic): dic["link_datetime_max"] = data_type_detail_form["datetime_max"].initial
                            if("link_datetime_step" not in dic): dic["link_datetime_step"] = data_type_detail_form["datetime_step"].initial
            
            # JSからのデータはリストで渡されるため、扱いやすいよう変換: ["aaaaa"] -> "aaaaa"
            for k in dic.keys():
                if(dic[k].__class__ is list):
                    dic[k] = dic[k][0]
            create_data = CreateData()

            # JSONの生成
            if( dic.keys() >= {"column_name", "column_type", "data_type"}):
                if (dic["column_type"] == "normal"):
                    if("generate_type" in dic): # product か random の判定は不要
                        if (dic["data_type"] == "string"): # textがあるかの判定も必要？
                            create_data.create_list(dic["column_name"], dic["generate_type"], dic["text"].split("\n"))
                        if (dic["data_type"] == "number"):
                            create_data.create_amount(dic["column_name"], dic["generate_type"], float(dic["number_min"]), float(dic["number_max"]), float(dic["number_step"]))
                        if (dic["data_type"] == "date"):
                            create_data.create_date(dic["column_name"], dic["generate_type"], dic["date_min"], dic["date_max"], int(dic["date_step"]))
                        if (dic["data_type"] == "datetime"):
                            create_data.create_datetime(dic["column_name"], dic["generate_type"], dic["datetime_min"], dic["datetime_max"], int(dic["datetime_step"]))
                if (dic["column_type"] == "link"):
                    if("link_column_name" in dic): # product か random の判定は不要
                        if (dic["data_type"] == "string"): # textがあるかの判定も必要？
                            create_data.create_link_list(dic["column_name"], dic["link_column_name"], dic["link_text"].split("\n"))
                        if (dic["data_type"] == "number"):
                            create_data.create_link_amount(dic["column_name"], dic["link_column_name"], float(dic["link_number_min"]), float(dic["link_number_max"]), float(dic["link_number_step"]))
                        if (dic["data_type"] == "date"):
                            create_data.create_link_date(dic["column_name"], dic["link_column_name"], dic["link_date_min"], dic["link_date_max"], int(dic["link_date_step"]))
                        if (dic["data_type"] == "datetime"):
                            create_data.create_link_datetime(dic["column_name"], dic["link_column_name"], dic["link_datetime_min"], dic["link_datetime_max"], int(dic["link_datetime_step"]))
            print("output: ", create_data.data)
            if(len(create_data.data.keys()) != 0):
                mylogger.info(log_format.format(
                    client_ip = request.META.get('REMOTE_ADDR'), 
                    column_name = create_data.data["column_name"],
                    data_length = len(create_data.data["generate_data"]),
                    sample = create_data.data["generate_data"] if len(create_data.data["generate_data"]) < num_pick_up_samples else create_data.data["generate_data"][0:num_pick_up_samples]
                    ))
            output_json = json.dumps(create_data.data, ensure_ascii=False)
            d = {
                'generate_type_form': str(column_type_form),
                'data_detail': str(data_type_detail_form),
                'gen_button': '<button type="button" class="button-lg button is-danger" onclick=send_data_detail() name="generate" >Generate</button>',
                'output_json' : output_json
            }
            return JsonResponse(d)
        
        else:
            return render(request, 'create.html', {
                "column_name_form" : ColumnNameForm(),
                "column_type_form" : ColumnTypeForm(),
            })
    return render(request, 'create.html', {
        "column_name_form" : ColumnNameForm(),
        "column_type_form" : ColumnTypeForm(),
    })

def check(request):
    return render(request, 'check.html', {})