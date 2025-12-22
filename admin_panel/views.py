from django.shortcuts import render,redirect
<<<<<<< HEAD

from django.contrib.auth import authenticate,login,logout

=======
<<<<<<< HEAD
from django.contrib.auth import authenticate,login,logout
=======
from django.contrib.auth import authenticate,login
>>>>>>> 93a7b86ed4178619cc4bc13f8f0f6141663a87af
>>>>>>> cb1b3181f1be4f3ce5ea799625050162a878655a
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
<<<<<<< HEAD

		return render(request ,"admin_panel/Login.html",{
			'error':'Incorrect admin credentials'})
	return render(request,'admin_panel/Login.html')
=======
<<<<<<< HEAD
		return render(request ,"admin_panel/Login.html",{
			'error':'Incorrect admin credentials'})
	return render(request,'admin_panel/Login.html')
=======
		return render(request ,"admin_panel/login.html",{
			'error':'Incorrect admin credentials','username':username,'password': password})
	return render(request,'admin_panel/login.html')
>>>>>>> 93a7b86ed4178619cc4bc13f8f0f6141663a87af
>>>>>>> cb1b3181f1be4f3ce5ea799625050162a878655a


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

<<<<<<< HEAD

=======
<<<<<<< HEAD
>>>>>>> cb1b3181f1be4f3ce5ea799625050162a878655a
	return render(request,'admin_panel/admin_dashboard.html',context);

def admin_logout(request):
	logout(request)
<<<<<<< HEAD
	return render(request,'admin_panel/logout.html')
=======
	return render(request,'admin_panel/logout.html')
=======
	return render(request,'admin_panel/admin_dashboard.html',context);
>>>>>>> 93a7b86ed4178619cc4bc13f8f0f6141663a87af
>>>>>>> cb1b3181f1be4f3ce5ea799625050162a878655a
