from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Product



def index(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'inventory/index.html', context)


def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'inventory/detail.html', {'product': product})
