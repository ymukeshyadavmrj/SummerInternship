from django.urls import path
from appfour import views

urlpatterns = [
    path('',views.form_fn,name='something')
]
