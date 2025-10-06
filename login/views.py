from django.shortcuts import render

# Create your views here.

def login_pagina(request):
    return render(request, 'loginPagina.html')