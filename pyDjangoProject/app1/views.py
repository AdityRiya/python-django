
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    my_dict = {'insert_me':"hello"}
    return render(request,'First File/index.html',context=my_dict)