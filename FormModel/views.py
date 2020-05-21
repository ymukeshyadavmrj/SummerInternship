from django.shortcuts import render
from FormModel.forms import NewUser

# Create your views here.
def newusers(request):
    form = NewUser()

    if request.method == "POST":
        form = NewUser(request.POST)
        if form.is_valid():
            form.save(commit=True)
        else:
            print("Error form invalid")

    return render(request,"FormModel/form_page.html",{'form':form})
