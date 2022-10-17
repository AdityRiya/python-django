
from django.shortcuts import render
from django.http import HttpResponse
from app1.models import Topic,AccessRecord,Webpage
# Create your views here.
def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records':webpages_list}
    
   
    return render(request,'First File/index.html',context=date_dict)
    
def help(request):
     help = {'help': " helping with the django projct"}
     return render(request,'Help/help.html',context=help)