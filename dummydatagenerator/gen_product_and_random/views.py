from django.shortcuts import render
from .models import Post
from django.shortcuts import redirect
from .forms import DocumentForm

# Create your views here.
def frontpage(request):
    posts = Post.objects.all()
    print(posts.values())
    return render(request, "frontpage.html", {"posts": posts})

    # if request.method == 'POST':
    #     form = DocumentForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('https://www.youtube.com/watch?v=O037g3NOoXY')
    # else:
    #     form = DocumentForm()
    # return render(request, 'frontpage.html', {
    #     'form': form
    # })