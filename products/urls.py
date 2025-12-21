from django.urls import path
from . import views
from .views import (CategoryListView,AddCategory,EditCategory,DeleteCategory,SubCategoryListView,AddSubCategory,
DeleteSubCategory,EditSubCategory,ProductListView,AddProduct,EditProduct,DeleteProduct)


app_name='admin_panel'
urlpatterns = [
    path('category/', CategoryListView.as_view(), name='category_list'),
   
    path('category/add/',AddCategory.as_view(),name ="category_add"),
    path('category/edit/<slug:slug>/',EditCategory.as_view(),name ="category_edit"),
    path('category/delete/<slug:slug>/',DeleteCategory.as_view(),name ="category_delete"),
    path('subcategory/', SubCategoryListView.as_view(), name='subcategory_list'),
    path('subcategory/add/',AddSubCategory.as_view(),name ="subcategory_add"),
    path('subcategory/edit/<slug:slug>/',EditSubCategory.as_view(),name ="subcategory_edit"),
    path('subcategory/delete/<slug:slug>/',DeleteSubCategory.as_view(),name ="subcategory_delete"),
    path('product/', ProductListView.as_view(), name='product_list'),
    path('product/add/',AddProduct.as_view(),name ="product_add"),
    path('product/edit/<str:sku>/',EditProduct.as_view(),name ="product_edit"),
    path('product/delete/<str:sku>/',DeleteProduct.as_view(),name ="product_delete"),
]
