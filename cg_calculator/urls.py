
from django.urls import path,include
from . import views
urlpatterns = [
    path("",views.cg_calculator,name="cg_calculator")
]