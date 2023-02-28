from django.shortcuts import render, get_object_or_404
from .models import Post
from django.shortcuts import redirect
from .forms import DocumentForm
from django.http import HttpResponse
from .prod_and_random import DummyDataGenerator
import json


# Create your views here.
def product_and_random(request):
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
                return render(request, 'product_and_random.html', {
                    "text": text,
                    'form': form
                })
        elif "generate" in request.POST:
            print("generate!")
            with posts[len(posts) - 1].document.open("r") as f:
                data = json.load(f)
            dummydata_generator = DummyDataGenerator(str(posts[len(posts) - 1].document.file))
            dummydata_generator.json_check()
            dummydata_generator.prepare_prod_and_random()
            dummydata_generator.make_product_data()
            dummydata_generator.make_random_data()
            # dummydata_generator.output_csv(output_path)
            with posts[len(posts) - 1].document.open("r") as f:
                text = f.read()
            return render(request, 'product_and_random.html', {
                    "text" : text,
                    "dataframe": dummydata_generator.df.to_html(),
                    'form': DocumentForm()
            })

        elif "download_csv" in request.POST:
            with posts[len(posts) - 1].document.open("r") as f:
                data = json.load(f)
            dummydata_generator = DummyDataGenerator(str(posts[len(posts) - 1].document.file))
            dummydata_generator.json_check()
            dummydata_generator.prepare_prod_and_random()
            dummydata_generator.make_product_data()
            dummydata_generator.make_random_data()
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename=filename.csv'
            dummydata_generator.df.to_csv(path_or_buf=response, sep=',', float_format='%.2f', index=False, decimal=",")
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