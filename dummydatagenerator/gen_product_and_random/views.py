from django.shortcuts import render, get_object_or_404
from .models import Post
from django.shortcuts import redirect
from .forms import DocumentForm
from django.http import HttpResponse
from .prod_and_random import DummyDataGenerator
import json
import pandas as pd
import io

JSON_FILENAME = ""
JSON_TEXT = ""
OUTPUT_DF = pd.DataFrame()

# Create your views here.
def product_and_random(request):
    global JSON_FILENAME, JSON_TEXT, OUTPUT_DF
    if request.method == 'POST':
        if "submit" in request.POST:
            form = DocumentForm(request.POST, request.FILES)
            if form.is_valid():
                JSON_FILENAME = request.FILES['document']
                JSON_TEXT = request.FILES['document'].read().decode('utf-8')
                dummydata_generator = DummyDataGenerator()
                try:
                    dummydata_generator.read_from_jsontext(JSON_TEXT)
                except:
                    return render(request, 'product_and_random.html', {
                    "file": JSON_FILENAME,
                    "text": "",
                    'form': form,
                    "error_msg": {"JSON_error": "JSONの形式になっていない可能性があります。ファイルを確認してください。"}
                })
                dummydata_generator.json_check()
                json_dict = json.loads(JSON_TEXT)
                return render(request, 'product_and_random.html', {
                    "file": JSON_FILENAME,
                    "text": json_dict,
                    'form': form,
                    "error_msg": dummydata_generator.error_msg_dict
                })
        elif "generate" in request.POST:
            # if (len(JSON_TEXT) == 0):
            #     return render(request, 'product_and_random.html', {
            #         "text": "",
            #         'form': DocumentForm()
            #     })
            print("generate!")
            dummydata_generator = DummyDataGenerator()
            dummydata_generator.read_from_jsontext(JSON_TEXT)
            dummydata_generator.json_check()
            json_dict = json.loads(JSON_TEXT)
            dummydata_generator.prepare_prod_and_random()
            dummydata_generator.make_product_data()
            dummydata_generator.make_random_data()
            OUTPUT_DF = dummydata_generator.df
            return render(request, 'product_and_random.html', {
                "file":  JSON_FILENAME,
                "text" : "wwww",
                "dataframe": OUTPUT_DF.head(10).to_html(classes=["table", "table-bordered", "table-hover, overflow-scroll"]),
                'form': DocumentForm()
            })

        elif "download_csv" in request.POST:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename=filename.csv'
            OUTPUT_DF.to_csv(path_or_buf=response, sep=',', float_format='%.2f', index=False, decimal=",")
            return response
    else:
        form = DocumentForm()
    return render(request, 'product_and_random.html', {
        'form': form
    })