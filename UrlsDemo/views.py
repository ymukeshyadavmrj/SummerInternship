from django.shortcuts import render

# Create your views here.
def index(request):
    my_dict = {'text':'Hello World','number':100}
    return render(request,"UrlsDemo/index.html",my_dict)

def other(request):
    return render(request,"UrlsDemo/others.html")

def relative(request):
    return render(request,"UrlsDemo/relative.html")
