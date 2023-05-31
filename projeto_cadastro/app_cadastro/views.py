# Create your views here.
from django.shortcuts import render
def home(request): # consultará arquivo 'url' e fará uma requisição
    return render(request, 'produtos/home.html')


