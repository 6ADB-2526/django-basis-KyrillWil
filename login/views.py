from django.shortcuts import render

# Create your views here.

def loginPagina(request):
    return render(request, 'startPagina.html')