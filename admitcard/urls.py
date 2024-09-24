
from django.urls import path
from . import views
from django.shortcuts import render,HttpResponse

urlpatterns = [
    path('', views.admit_card_form, name='admit_card_form'),
    path('success/', lambda request: HttpResponse("Success!"), name='success'),
    path('admit/<int:admit_card_id>/preview/', views.admit_preview, name='admit_preview'),
    path('admit/pdf/<int:admit_card_id>/', views.generate_admit_card_pdf, name='generate_admit_card_pdf'),
]