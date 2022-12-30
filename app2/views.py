from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def jinja_print(request):
    d={'age':'21'}
    return render(request,'jinja2.html',context=d)