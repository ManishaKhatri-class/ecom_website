from django.shortcuts import render
from products.models import Category,SubCategory,Product
from products.forms import CategoryForm,SubCategoryForm,ProductForm
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.views.generic import (ListView,
	CreateView,
	UpdateView,
	DeleteView)
from django.urls import reverse_lazy


class  CategoryListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
	model=Category
	form_class=CategoryForm
	template_name='admin_panel/category_list.html'
	success_url= reverse_lazy('admin_panel:admin-dashoard')
	context_object_name='categories'
	permission_required='admin_panel.view_category'

class  AddCategory(LoginRequiredMixin,CreateView,PermissionRequiredMixin):
	model=Category
	form_class=CategoryForm
	template_name='admin_panel/category_add.html'
	success_url= reverse_lazy('admin_panel:category_list')
	permission_required='admin_panel.add_category'



class EditCategory(LoginRequiredMixin,UpdateView,PermissionRequiredMixin):
	model=Category
	form_class=CategoryForm
	template_name='admin_panel/category_edit.html'
	slug_field='slug'
	slug_url_kwarg='slug'
	success_url=reverse_lazy('admin_panel:category_list')
	permission_required='admin_panel.edit_category'
	

class DeleteCategory(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
	model=Category
	template_name='admin_panel/category_delete.html'
	slug_field='slug'
	slug_url_kwarg='slug'
	success_url= reverse_lazy('admin_panel:category_list')
	permission_required='admin_panel.delete_category'

class  SubCategoryListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
	model=SubCategory
	form_class=SubCategoryForm
	template_name='admin_panel/subcategory_list.html'
	success_url= reverse_lazy('admin_panel:admin-dashoard')
	context_object_name='subcategories'
	permission_required='admin_panel.view_subcategory'

class  AddSubCategory(LoginRequiredMixin,CreateView,PermissionRequiredMixin):
	model=SubCategory
	form_class=SubCategoryForm
	template_name='admin_panel/subcategory_add.html'
	success_url= reverse_lazy('admin_panel:subcategory_list')
	permission_required='admin_panel.add_subcategory'



class EditSubCategory(LoginRequiredMixin,UpdateView,PermissionRequiredMixin):
	model=SubCategory
	form_class=SubCategoryForm
	template_name='admin_panel/subcategory_edit.html'
	slug_field='slug'
	slug_url_kwarg='slug'
	success_url=reverse_lazy('admin_panel:subcategory_list')
	permission_required='admin_panel.edit_subcategory'
	

class DeleteSubCategory(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
	model=SubCategory
	template_name='admin_panel/subcategory_delete.html'
	slug_field='slug'
	slug_url_kwarg='slug'
	success_url= reverse_lazy('admin_panel:subcategory_list')
	permission_required='admin_panel.delete_subcategory'


class  ProductListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
	model=Product
	form_class=ProductForm
	template_name='admin_panel/product_list.html'
	success_url= reverse_lazy('admin_panel:admin-dashoard')
	context_object_name='products'
	permission_required='admin_panel.view_product'

class  AddProduct(LoginRequiredMixin,CreateView,PermissionRequiredMixin):
	model=Product
	form_class=ProductForm
	template_name='admin_panel/product_add.html'
	success_url= reverse_lazy('admin_panel:product_list')
	permission_required='admin_panel.add_product'



class EditProduct(LoginRequiredMixin,UpdateView,PermissionRequiredMixin):
	model=Product
	form_class=ProductForm
	template_name='admin_panel/product_edit.html'
	slug_field='sku'
	slug_url_kwarg='sku'
	success_url=reverse_lazy('admin_panel:product_list')
	permission_required='admin_panel.edit_product'
	

class DeleteProduct(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
	model=Product
	template_name='admin_panel/product_delete.html'
	slug_field='sku'
	slug_url_kwarg='sku'
	success_url= reverse_lazy('admin_panel:product_list')
	permission_required='admin_panel.delete_product'
