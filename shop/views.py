from django.shortcuts import render, get_object_or_404
from .models import Category, Product


# Create your views here.
def home(request, category_slug=None):
    category_page = None
    if category_slug is not None:
        category_page = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category_page)
    else:
        products = Product.objects.all()
    return render(request, 'shop/home.html', {'category': category_page, 'products': products})


def product(request):
    return render(request, 'shop/product.html')