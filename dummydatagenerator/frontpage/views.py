from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class frontpage(TemplateView):
    template_name = 'frontpage.html'