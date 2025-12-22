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