from .models import Product, CartOrder, CartOrderItems, Category, WishList, Vendor, ProductImages, ProductReview, Address

def default(request):
    categories = Category.objects.all()
    address = Address.objects.get(user=request.user)
    return {
        'categories': categories,
        'address': address,
    }