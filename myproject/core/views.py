from django.shortcuts import render
from django.contrib import messages
from django.contrib.messages import constants
from myproject.core.models import Product

# Create your views here.

def home(request):
    messages.add_message(request, constants.SUCCESS, 'Página carregada com sucesso')
    return render(request,'index.html')


def listar_produtos(request):
    produtos = Product.objects.all()    
    return render(request,'listar_produtos.html',  {'produtos':produtos})
