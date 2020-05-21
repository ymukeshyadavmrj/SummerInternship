from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic,Webpage,AccessRecord
# Create your views here.
def index(request):
    webpg_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records':webpg_list}
    return render(request,"temp/index1.html",context=date_dict)
