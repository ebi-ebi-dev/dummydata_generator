from django.shortcuts import render, get_object_or_404
from .models import Post
from django.shortcuts import redirect
from .forms import DocumentForm

# Create your views here.
def frontpage(request):
    posts = Post.objects.all()
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        print(form["document"]) 
        if form.is_valid():
            form.save()
            tmp2 = posts.exclude(id = posts.latest('id').id)
            for tmp in tmp2:
                delete(tmp.id)
            print(posts)
            with posts[len(posts) - 1].document.open("r") as f:
                text = f.read()
            return render(request, 'frontpage.html', {
                "text": text,
                'form': form
            })
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