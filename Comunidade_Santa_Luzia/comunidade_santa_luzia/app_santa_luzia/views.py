from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'comunidade/home.html')

def contatos(request):
    return render(request, 'comunidade/contatos.html')

def pastorais(request):
    return render(request, 'comunidade/pastorais.html')