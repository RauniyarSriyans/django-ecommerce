from .models import Product, CartOrder, CartOrderItems, Category, WishList, Vendor, ProductImages, ProductReview, Address

def default(request):
    categories = Category.objects.all()
    
    try:
        address = Address.objects.get(user=request.user)
    except:
        address = None
    
    return {
        'address': address, 
        'categories': categories,
    }
        
    