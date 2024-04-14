from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from taggit.models import Tag
from django.db.models import Count, Avg

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

def vendor_list_view(request):
    vendor = Vendor.objects.all()
    
    context = {
        'vendors': vendor,
    }
    
    return render(request, 'baseapp/vendor-list.html', context)

def vendor_detail_view(request, pk):
    vendor = Vendor.objects.get(vendor_id=pk)
    products = Product.objects.filter(vendor=vendor, product_status="published")
    
    context = {
        'vendor': vendor,
        'products': products,
    }
    
    return render(request, 'baseapp/vendor-detail.html', context)

def product_detail_view(request, pk):
    product = Product.objects.get(product_id=pk)
    # products = Product.objects.filter(vendor=vendor, product_status="published")
    p_images = product.p_images.all()
    
    products = Product.objects.filter(category=product.category).exclude(product_id=pk)
    
    # Getting all reviews
    reviews = ProductReview.objects.filter(product=product).order_by("-date")
    
    # Getting average reviews
    average_rating = ProductReview.objects.filter(product=product).aggregate(rating=Avg('rating'))
    
    context = {
        'product': product,
        'p_images': p_images,
        'products': products,
        'reviews': reviews,
        'average_rating': average_rating,
    }
    
    return render(request, 'baseapp/product-detail.html', context)
    
def tag_list_view(request, tag_slug=None):
    products = Product.objects.filter(product_status="published").order_by("-id")
    tag = None 
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        products = products.filter(tags__in=[tag])
    
    context = {
        "products": products, 
        "tag": tag,
    }
    
    return render(request, "baseapp/tag.html", context)
