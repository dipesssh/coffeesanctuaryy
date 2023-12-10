from django import views
from django.urls import path
from sanctuary.views import index

app_name = "sanctuary"

urlpatterns =[
    path("", index)
]