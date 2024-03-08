from django.shortcuts import render
from django.http import HttpResponse
from myproject.core.models import Product
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

def checar_produto(request):
    produto = request.GET.get('product')
    produtos = Product.objects.filter(name=produto)
    # if produtos.exists():
    #     return HttpResponse("Esse produto já existe.")    
    # return HttpResponse("Produto disponível para cadastro.")    

    return render(request,'partials/htmx_components/check_product.html', {'produtos':produtos})



def salvar_produto(request):
    produto = request.POST.get('product')
    preco = request.POST.get('price')

    novo_produto = Product(
        name = produto,
        price = preco
    )
    novo_produto.save()
    produtos = Product.objects.all()    
    return render(request,'partials/htmx_components/list_all_products.html',  {'produtos':produtos})

@csrf_exempt
@require_http_methods(['DELETE'])
def deletar_produto(request, id):
    deletar_produto = Product.objects.get(id=id)

    deletar_produto.delete()

    produtos = Product.objects.all()    
    return render(request,'partials/htmx_components/list_all_products.html',  {'produtos':produtos})
