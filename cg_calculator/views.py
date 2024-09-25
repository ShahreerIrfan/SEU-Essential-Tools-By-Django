from django.shortcuts import render

# Create your views here.

def cg_calculator(request):
    return render(request,"cg_calculator/cg_calculator.html")