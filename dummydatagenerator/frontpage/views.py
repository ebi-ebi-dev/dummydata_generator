from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class frontpage(TemplateView):
    template_name = 'frontpage.html'

class how_to_use(TemplateView):
    template_name = 'how_to_use.html'