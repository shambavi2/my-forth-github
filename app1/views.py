from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def jinja_print(request):
    d={'name':'shambhavi'}
    return render(request,'jinja_print.html',context=d)