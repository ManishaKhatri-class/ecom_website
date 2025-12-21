from django.shortcuts import render,redirect
from .forms import RegisterationForm
from django.views import View
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required,user_passes_test
from .models import Register
from django.contrib import messages



def user_register(request):
	form=RegisterationForm
	template='user/user_register.html'
	if request.method =="POST":
		fullname=request.POST.get('name').strip()
		email=request.POST.get('email').strip()
		mobile_number=request.POST.get('mobile_number').strip()
		password=request.POST.get('password').strip()
		confirm_password=request.POST.get('confirm_password').strip()
		
		if password!=confirm_password:
			return render(request,'user/user_register.html',{'error':'Passwords do not match'})
		if 	User.objects.filter(email=email).exists():
			return render(request,'user/user_register.html',{'error':'Email already exists'})

			#create user
		user=User.objects.create_user(username=email,email=email,password=password,full_name=fullname)
		message.success(request,'Registration Successful.Please login')
		return redirect('user_login')
	return render(request,'user/user_register.html')
			

def user_login(request):
	if request.method =="POST":
		email=request.POST.get('email').strip()
		password=request.POST.get('password').strip()
		try:

			user_obj =User.objects.get(email=email)
			user=authenticate(request,username=user_obj.username,password=password)
			print(user)
		except User.DoesNotExist:
				user=None
				if user is None :
					login(request,username)
					return redirect('user_dashboard')	
				return render(request,'user_login.html',{'error':'Invalid email or password'})
		return render(request,'user/user_login.html')



@login_required

def user_dashboard(request):
	return render(request,'user_dashboard.html')

def user_logout(request):
	logout(request)
	return render(request,'user_logout.html')