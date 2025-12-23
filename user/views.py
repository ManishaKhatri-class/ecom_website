
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from .forms import UserRegistrationForm,LoginForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import CustomUser
def user_register(request):
    if request.method == 'POST':
    	form = UserRegistrationForm(request.POST)
    	if form.is_valid():
    		user = User.objects.create_user(
    			username=form.cleaned_data['username'],
            	email=form.cleaned_data['email'],
            	password=form.cleaned_data['password']
            	)
    		CustomUser.objects.create(
            	user=user,
            	mobile_number=form.cleaned_data['mobile_number']
            	)
    		messages.success(request, "Account created successfully! Please login.")
    		return redirect('user-login')
    	else:
    	 return render(request, 'user/user_register.html', {'form': form})
    else:
    	form = UserRegistrationForm()
    	return render(request, 'user/user_register.html', {'form': form})


def user_login(request):

    if request.method == 'POST':
    	form = LoginForm(request.POST)
    	username_or_email = request.POST.get('username_or_email')
    	password = request.POST.get('password')
    	try:
    		user_obj = User.objects.get(username=username_or_email)
    	except User.DoesNotExist:
    		try:
    			user_obj = User.objects.get(email=username_or_email)
    		except User.DoesNotExist:
    			user_obj = None

    	if user_obj:
    		user = authenticate(request, username=user_obj.username, password=password)
    		if user:
    			login(request, user)
    			return redirect('user-dashboard')
    		else:
    			messages.error(request, "Incorrect password")
    	else:
    		messages.error(request, "User not found")
    		return render(request, 'user/user_login.html',{'form': form})
    else:
    	form = LoginForm()
    	return render(request, 'user/user_login.html',{'form': form})



@login_required
def user_dashboard(request):
    products = Product.objects.all()
    return render(request,'user/user_dashboard.html')

def user_logout(request):
    logout(request)
    return render(request,'admin_panel/Base.html')
@login_required
def profile(request):
    profile = CustomUser.objects.get(user=request.user)

    if request.method == 'POST':
        mobile_number = request.POST.get('mobile_number')
        if mobile_number and mobile_number != profile.mobile_number:
            # Check for uniqueness
            if CustomUser.objects.filter(mobile_number=mobile_number).exists():
                messages.error(request, "Mobile number already exists")
            else:
                profile.mobile_number = mobile_number
                profile.save()
                messages.success(request, "Profile updated successfully")
                return redirect('user-dashboard')

    return render(request, 'user/profile.html', {'profile': profile})
