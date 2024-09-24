
from django.urls import path
from . import views
from django.shortcuts import render,HttpResponse

urlpatterns = [
    path('', views.admit_card_form, name='admit_card_form'),
     path('success/', lambda request: HttpResponse("Success!"), name='success'),
]