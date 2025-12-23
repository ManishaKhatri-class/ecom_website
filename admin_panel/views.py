from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required,user_passes_test
from products.models import Category,SubCategory,Product


def admin_login(request):
	if request.method =="POST":
		username=request.POST.get('username').strip()
		password=request.POST.get('password').strip()
		user =authenticate(request,username=username,password=password)
		print(user)
		if user is not None and user.is_staff:
			login(request,user)
			return redirect('admin-dashboard')
		return render(request ,"admin_panel/login.html",{
			'error':'Incorrect admin credentials','username':username,'password': password})
	return render(request,'admin_panel/login.html')

def is_admin(user):
	return user.is_staff


@login_required
@user_passes_test(is_admin)
def admin_dashboard(request):

	context={
	'category_count':Category.objects.count(),
	'sub_category_count':SubCategory.objects.count(),
	'product_count':Product.objects.count(),
	'products':Product.objects.order_by('-id')[:5],
	}
	return render(request,'admin_panel/admin_dashboard.html',context)

def admin_logout(request):
	logout(request)
	return render(request,'admin_panel/admin_dashboard.html')
def home(request):
	return render(request,'admin_panel/Base.html')