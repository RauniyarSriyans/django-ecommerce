from django.contrib import admin
from django.urls import path
from baseapp import views

app_name = "baseapp"

urlpatterns = [
    path("", views.index, name="index"),
    path("category/", views.category_list_view, name="category-list"),
    path("category/<pk>/", views.product_list_category_view, name="category-product-list"),
    path("products/", views.product_list_view, name="product-list"),
]