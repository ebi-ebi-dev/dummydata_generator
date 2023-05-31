from django.shortcuts import render, get_object_or_404
from .models import Post
from django.shortcuts import redirect
from .forms import DocumentForm, JSONForm
from django.http import HttpResponse
from .prod_and_random import DummyDataGenerator
import json
import pandas as pd
import io

import dummydatagenerator.my_logger as my_logger
mylogger = my_logger.my_logger()
log_format = """[gen_product_and_random] {client_ip} > {msg}"""

JSON_TEXT = ""
INPUT_JSON_FROM = None
OUTPUT_DF = pd.DataFrame()
VIEW_TABLE_THRESHOLD = 10

# Create your views here.
def product_and_random(request):
    global JSON_TEXT, INPUT_JSON_FROM, OUTPUT_DF
    if request.method == 'POST':
        if "check" in request.POST: 
            JSON_TEXT = request.POST["text"]
            INPUT_JSON_FROM = JSONForm(request.POST)
            dummydata_generator = DummyDataGenerator()
            try:
                dummydata_generator.read_from_jsontext(JSON_TEXT)
            except:
                mylogger.error(log_format.format(
                    client_ip = request.META.get('REMOTE_ADDR'),
                    msg = "JSON check does not passed. "
                    ))
                return render(request, 'product_and_random.html', {
                "JSON_text_area": JSONForm(request.POST),
                "error_msg": {"JSON_error": "JSONの形式になっていない可能性があります。テキストエリアを確認してください。"},
                "checked_flag" : True,
            })
            dummydata_generator.json_check()
            mylogger.info(log_format.format(
                client_ip = request.META.get('REMOTE_ADDR'),
                msg = "JSON check passed. "
                ))
            
            return render(request, 'product_and_random.html', {
                "JSON_text_area": JSONForm(request.POST),
                "error_msg": dummydata_generator.error_msg_dict,
                "checked_flag" : True,
                })
        elif "generate" in request.POST:
            dummydata_generator = DummyDataGenerator()
            dummydata_generator.read_from_jsontext(JSON_TEXT)
            dummydata_generator.json_check()
            
            dummydata_generator.prepare_prod_and_random()
            dummydata_generator.make_product_data()
            dummydata_generator.make_random_data()
            OUTPUT_DF = dummydata_generator.df

            if(len(OUTPUT_DF) < VIEW_TABLE_THRESHOLD ):
                mylogger.info(log_format.format(
                    client_ip = request.META.get('REMOTE_ADDR'),
                    msg = f"generate CSV \n {OUTPUT_DF.head()}"
                    ))
                return render(request, 'product_and_random.html', {
                    "JSON_text_area": INPUT_JSON_FROM,
                    "dataframe_head": OUTPUT_DF.head(VIEW_TABLE_THRESHOLD).to_html(classes=["table", "table-bordered", "table-hover, overflow-scroll"]),
                    "dataframe_tail": "",
                    "checked_flag" : True,
                })
            else:
                return render(request, 'product_and_random.html', {
                    "JSON_text_area": INPUT_JSON_FROM,
                    "dataframe_head": OUTPUT_DF.head(VIEW_TABLE_THRESHOLD).to_html(classes=["table", "table-bordered", "table-hover, overflow-scroll"]),
                    "dataframe_tail": OUTPUT_DF.tail(VIEW_TABLE_THRESHOLD).to_html(classes=["table", "table-bordered", "table-hover, overflow-scroll"]),
                    "checked_flag" : True,
                })

        elif "download_csv" in request.POST:
            mylogger.info(log_format.format(
                client_ip = request.META.get('REMOTE_ADDR'),
                msg = "CSV downloaded. "
                ))
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename=filename.csv'
            OUTPUT_DF.to_csv(path_or_buf=response, sep=',', index=False)
            return response
    else:
        pass
    return render(request, 'product_and_random.html', {
        "JSON_text_area" : JSONForm(request.POST)
    })