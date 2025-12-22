<<<<<<< HEAD
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm

from django.contrib.auth.decorators import login_required

def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)              
            user.set_password(form.cleaned_data['password1'])  
            user.save() 
            email = form.cleaned_data.get('email')
            messages.success(request, f'Your account has been created, {email}! You can now log in.')
            return redirect('user-login')
    else:
        form = UserRegistrationForm()
    return render(request, 'user/user_register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')
        try:
            user = CustomUser.objects.get(username=username)
            if user.check_password(password):
                request.session['user_id'] = user.id  
                return redirect('user-dashboard')
            else:
                error = "Incorrect password"
        except CustomUser.DoesNotExist:
            error = "User not found"

        return render(request, 'users/user_login.html', {'error': error})
    return render(request, 'users/user_login.html')


@login_required
def user_dashboard(request):

    return render(request,'user/user_dashboard.html')

def user_logout(request):
    logout(request)
    return redirect('user-logout')
=======
<<<<<<< HEAD
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
=======
from django.shortcuts import render

# Create your views here.
>>>>>>> 93a7b86ed4178619cc4bc13f8f0f6141663a87af
>>>>>>> cb1b3181f1be4f3ce5ea799625050162a878655a
