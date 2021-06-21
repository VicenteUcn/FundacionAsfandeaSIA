from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'inicio.html')

def infantil(request):
    return render(request, 'infantil.html')

def apoderados(request):
    return render(request, 'apoderados.html')

def calendario(request):
    return render(request, 'calendario.html')

def programas(request):
    return render(request, 'programas.html')
