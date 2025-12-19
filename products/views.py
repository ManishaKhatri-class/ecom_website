from django.shortcuts import render
from products.models import Category,SubCategory,Product
from products.forms import CategoryForm


def category_list(request):
	categories=Category.objects.all()
	return render(request,'admin_panel/category_list.html')

def category_add(request):
	forms=CategoryForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('category_list')
	return render(request,'admin_panel/category_list.html',{'form':form})
	