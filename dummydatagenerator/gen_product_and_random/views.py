from django.shortcuts import render, get_object_or_404
from .models import Post
from django.shortcuts import redirect
from .forms import DocumentForm
from django.http import HttpResponse

# Create your views here.
def frontpage(request):
    posts = Post.objects.all()
    if request.method == 'POST':
        if "submit" in request.POST:
            form = DocumentForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                with posts[len(posts) - 1].document.open("r") as f:
                    text = f.read()
                tmp2 = posts.exclude(id = posts.latest('id').id)
                for tmp in tmp2:
                    delete(tmp.id)
                return render(request, 'frontpage.html', {
                    "text": text,
                    'form': form
                })
        elif "generate" in request.POST:
            print("generate!")
            with posts[len(posts) - 1].document.open("r") as f:
                data = json.load(f)
            dummydata_generator = DummyDataGenerator(str(posts[len(posts) - 1].document.file))
            dummydata_generator.make_product_data()
            dummydata_generator.make_random_data()
            # dummydata_generator.output_csv(output_path)
            with posts[len(posts) - 1].document.open("r") as f:
                text = f.read()
            return render(request, 'frontpage.html', {
                    "text" : text,
                    "dataframe": dummydata_generator.df.to_html(),
                    'form': DocumentForm()
            })

        elif "download_csv" in request.POST:
            with posts[len(posts) - 1].document.open("r") as f:
                data = json.load(f)
            dummydata_generator = DummyDataGenerator(str(posts[len(posts) - 1].document.file))
            dummydata_generator.make_product_data()
            dummydata_generator.make_random_data()
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename=filename.csv'
            dummydata_generator.df.to_csv(path_or_buf=response, sep=',', float_format='%.2f', index=False, decimal=",")
            return response
    else:
        form = DocumentForm()
    return render(request, 'frontpage.html', {
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