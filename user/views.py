
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from .forms import UserRegistrationForm,LoginForm,ProfileUpdateForm,UserUpdateForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import CustomUser
from products.models import Product

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
        remember_me=request.POST.get('remember_me')
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
                    if remember_me=="on":
                        request.session.set_expiry(60*60*24*2)
                    else:
                        request.session.set_expiry(0)
                    return redirect('user-dashboard')
                else:
                    messages.error(request, "Incorrect password")
                    return redirect('user-login')
        else:
                messages.error(request, "User not found")
                return render(request, 'user/user_login.html',{'form': form})
    else:
        form = LoginForm()
        return render(request, 'user/user_login.html',{'form': form})



@login_required
def user_dashboard(request):
    products = Product.objects.all()
    return render(request,'user/user_dashboard.html',{'products':products})

def user_logout(request):
    logout(request)
    return redirect('home')
@login_required
def profile(request):
    
    if request.method == 'POST':
        u_form=UserUpdateForm(request.POST,instance=request.user)
        p_form=ProfileUpdateForm(
            request.POST,
            request.FILES,
            instance=request.user.customuser
            )
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,"Profile Updated Successfully!")
            return redirect('profile')
        else:
            u_form=UserUpdateForm(instance=request.user)
            p_form=ProfileUpdateForm(instance=request.user.customuser)
            messages.error(request,"Profile Not Updated")
            return render(request,'user/profile.html',context)
    else:
        u_form=UserUpdateForm(instance=request.user)
        p_form=ProfileUpdateForm(instance=request.user.customuser)
        context = {
        'u_form': u_form,
        'p_form': p_form,
        'profile': request.user.customuser
        }
        return render(request,'user/profile.html',context)
