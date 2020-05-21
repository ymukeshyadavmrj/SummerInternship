from django.shortcuts import render
from appfour.forms import FormName
from appfour.models import User

def form_fn(request):
    form = FormName()
    if request.method == 'POST':
        form = FormName(request.POST)

        if form.is_valid():
            t = User.objects.get_or_create(first_name=form.cleaned_data['first_name'],last_name=form.cleaned_data['last_name'],email=form.cleaned_data['email'])[0]
            t.save()
    return render(request,'appfour/form_page.html',{'form':form})
