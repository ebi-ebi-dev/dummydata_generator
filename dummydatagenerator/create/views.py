from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from .create import CreateData
from .models import CreateModel
from .forms import CreateForm

# Create your views here.
# class create(TemplateView):
#     template_name = 'create.html'

def create(request):
    posts = CreateModel.objects.all()
    
    print("posts: ")
    print(posts)
    forms = CreateForm(request.POST)
    if request.method == 'POST':
        
        print("forms: ")
        print(forms)
        return redirect('http://localhost:8000/create/check/')

    content = {
        "posts" : posts,
        "forms" : forms,
    }
    return render(request, 'create.html', content)

def check(request):
    return render(request, 'check.html', {})