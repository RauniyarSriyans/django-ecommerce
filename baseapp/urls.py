from django.contrib import admin
from django.urls import path
from baseapp import views

app_name = "baseapp"

urlpatterns = [
    path("", views.index, name="index"),
    
    path("products/", views.product_list_view, name="product-list"),
    path("product/<pk>/", views.product_detail_view, name="product-detail"),
    
    
    path("category/", views.category_list_view, name="category-list"),
    path("category/<pk>/", views.product_list_category_view, name="category-product-list"),
    
    path("vendors/", views.vendor_list_view, name="vendor-list"),
    path("vendor/<pk>/", views.vendor_detail_view, name="vendor-detail"),
    
    path("products/tag/<slug:tag_slug>/", views.tag_list_view, name="tags"),
]