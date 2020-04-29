"""定义网站逻辑的地方
"""
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')