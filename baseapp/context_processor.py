from .models import Product, CartOrder, CartOrderItems, Category, WishList, Vendor, ProductImages, ProductReview, Address

def default(request):
    categories = Category.objects.all()
    return {
        'categories': categories,
    }