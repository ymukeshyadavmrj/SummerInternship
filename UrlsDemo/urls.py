from django.urls import path
from UrlsDemo import views

app_name = 'UrlsDemo'

urlpatterns = [
    path('others/',views.other,name="other"),
    path('relative/',views.relative,name="relative")
]
