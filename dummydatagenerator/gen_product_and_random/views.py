from django.shortcuts import render, get_object_or_404
from .models import Post
from django.shortcuts import redirect
from .forms import DocumentForm
from django.http import HttpResponse
from .prod_and_random import DummyDataGenerator
import json
import pandas as pd
import io

JSON_TEXT = ""
OUTPUT_DF = pd.DataFrame()

# Create your views here.
def product_and_random(request):
    global JSON_TEXT, OUTPUT_DF
    posts = Post.objects.all()
    # print("rrrr: ", request.FILES['document'].read().decode('utf-8'))
    if request.method == 'POST':
        if "submit" in request.POST:
            form = DocumentForm(request.POST, request.FILES)
            if form.is_valid():
                # data = pd.read_csv(io.StringIO(request.FILES['document'].read().decode('utf-8')), delimiter=',')
                # form.save()
                # with posts[len(posts) - 1].document.open("r") as f:
                JSON_TEXT = request.FILES['document'].read().decode('utf-8')
                # print("json: ", json.loads(text))
                # print("data", data)
                dummydata_generator = DummyDataGenerator()
                dummydata_generator.read_from_jsontext(JSON_TEXT)
                dummydata_generator.json_check()
                json_dict = json.loads(JSON_TEXT)
                return render(request, 'product_and_random.html', {
                    "text": json_dict,
                    'form': form,
                    "error_msg": dummydata_generator.error_msg_dict
                })
        elif "generate" in request.POST:
            if (len(JSON_TEXT) == 0):
                return render(request, 'product_and_random.html', {
                    "text": "",
                    'form': DocumentForm()
                })
            print("generate!")
            dummydata_generator = DummyDataGenerator()
            dummydata_generator.read_from_jsontext(JSON_TEXT)
            dummydata_generator.json_check()
            json_dict = json.loads(JSON_TEXT)
            if(dummydata_generator.error_code != 0 ): 
                print(dummydata_generator.error_msg)
                json_dict = json.loads(JSON_TEXT)
            dummydata_generator.prepare_prod_and_random()
            dummydata_generator.make_product_data()
            dummydata_generator.make_random_data()
            OUTPUT_DF = dummydata_generator.df
            print(json_dict)
            return render(request, 'product_and_random.html', {
                    "text" : json_dict,
                    "dataframe": OUTPUT_DF.head(10).to_html(classes=["table", "table-bordered", "table-hover, overflow-scroll"]),
                    'form': DocumentForm()
            })

        elif "download_csv" in request.POST:
            # with posts[len(posts) - 1].document.open("r") as f:
            #     data = json.load(f)
            # dummydata_generator = DummyDataGenerator(str(posts[len(posts) - 1].document.file))
            # dummydata_generator.json_check()
            # dummydata_generator.prepare_prod_and_random()
            # dummydata_generator.make_product_data()
            # dummydata_generator.make_random_data()
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename=filename.csv'
            OUTPUT_DF.to_csv(path_or_buf=response, sep=',', float_format='%.2f', index=False, decimal=",")
            return response
    else:
        form = DocumentForm()
    return render(request, 'product_and_random.html', {
        "datas": posts,
        'form': form
    })

def delete(json_id=0):

    # Uploadjsonのインスタンスを取得
    upload_json = get_object_or_404(Post, id=json_id)

    # json ファイルの実体を削除
    upload_json.document.delete()
    
    # レコードの削除
    upload_json.delete()