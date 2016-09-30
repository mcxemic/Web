from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    def get(self,request,**kwargs):
        return render(request,'index.html',context=None)

class AboutPageView(TemplateView):
    template_name = 'about.html'

class LabPageView(TemplateView):
    template_name = 'lab2.html'