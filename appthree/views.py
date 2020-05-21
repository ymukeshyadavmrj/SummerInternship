from django.shortcuts import render
from appthree.forms import NewUserForm
# Create your views here.
def users(request):
    form = NewUserForm()
    if request.method == "POST" :
        form  = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
        else:
            print("Error FORM invalid")
    return render(request,'appthree/users.html',{'form':form})
