from django.shortcuts import render, get_object_or_404
from .models import Post
from django.shortcuts import redirect
from .forms import DocumentForm, JSONForm
from django.http import HttpResponse
from .prod_and_random import DummyDataGenerator
import json
import pandas as pd
import io

JSON_TEXT = ""
INPUT_JSON_FROM = None
OUTPUT_DF = pd.DataFrame()
VIEW_TABLE_THRESHOLD = 10

# Create your views here.
def product_and_random(request):
    global JSON_TEXT, INPUT_JSON_FROM, OUTPUT_DF
    print(request.POST)
    if request.method == 'POST':
        if "check" in request.POST: 
            JSON_TEXT = request.POST["text"]
            INPUT_JSON_FROM = JSONForm(request.POST)
            dummydata_generator = DummyDataGenerator()
            try:
                dummydata_generator.read_from_jsontext(JSON_TEXT)
            except:
                return render(request, 'product_and_random.html', {
                "JSON_text_area": JSONForm(request.POST),
                "error_msg": {"JSON_error": "JSONの形式になっていない可能性があります。テキストエリアを確認してください。"}
            })
            dummydata_generator.json_check()
            
            return render(request, 'product_and_random.html', {
                "JSON_text_area": JSONForm(request.POST),
                "error_msg": dummydata_generator.error_msg_dict
                })
        elif "generate" in request.POST:
            print("generate!")
            dummydata_generator = DummyDataGenerator()
            dummydata_generator.read_from_jsontext(JSON_TEXT)
            dummydata_generator.json_check()
            
            dummydata_generator.prepare_prod_and_random()
            dummydata_generator.make_product_data()
            dummydata_generator.make_random_data()
            OUTPUT_DF = dummydata_generator.df

            if(len(OUTPUT_DF) < VIEW_TABLE_THRESHOLD ):
                return render(request, 'product_and_random.html', {
                    "JSON_text_area": INPUT_JSON_FROM,
                    "dataframe_head": OUTPUT_DF.head(VIEW_TABLE_THRESHOLD).to_html(classes=["table", "table-bordered", "table-hover, overflow-scroll"]),
                    "dataframe_tail": "",
                })
            else:
                return render(request, 'product_and_random.html', {
                    "JSON_text_area": INPUT_JSON_FROM,
                    "dataframe_head": OUTPUT_DF.head(VIEW_TABLE_THRESHOLD).to_html(classes=["table", "table-bordered", "table-hover, overflow-scroll"]),
                    "dataframe_tail": OUTPUT_DF.tail(VIEW_TABLE_THRESHOLD).to_html(classes=["table", "table-bordered", "table-hover, overflow-scroll"]),
                })

        elif "download_csv" in request.POST:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename=filename.csv'
            OUTPUT_DF.to_csv(path_or_buf=response, sep=',', index=False)
            return response
    else:
        pass
    return render(request, 'product_and_random.html', {
        "JSON_text_area" : JSONForm(request.POST)
    })