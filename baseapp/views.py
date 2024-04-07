from django.shortcuts import render 
from django.http import HttpResponse

from .models import Product, CartOrder, CartOrderItems, Category, WishList, Vendor, ProductImages, ProductReview, Address

# Create your views here.
def index(request):
    products = Product.objects.filter(featured=True, product_status="published" ).order_by("-id")

    context = {
        'products': products
    }
    return render(request, 'baseapp/index.html', context)

def product_list_view(request):
    products = Product.objects.filter(product_status="published").order_by("-id")

    context = {
        'products': products
    }
    return render(request, 'baseapp/product-lists.html', context)

def category_list_view(request):
    categories = Category.objects.all()

    context = {
        "categories":categories
    }
    return render(request, 'baseapp/category-list.html', context)

def product_list_category_view(request, pk):
    category = Category.objects.get(category_id=pk)
    products = Product.objects.filter(product_status="published",category=category)

    context = {
        "products": products, 
        "category": category,
    }

    return render(request, 'baseapp/category-product-list.html', context)
