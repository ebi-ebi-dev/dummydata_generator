from django.shortcuts import render
from django.views.generic import TemplateView
from .create import CreateData
from .models import Post

# Create your views here.
class create(TemplateView):
    template_name = 'create.html'

# def create(request):
#     posts = Post.objects.all()
    