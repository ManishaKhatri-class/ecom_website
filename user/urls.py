from django.urls import path

from django.contrib import admin
from django.contrib.auth import views as auth_views
from user import views as user_views

urlpatterns=[

path('register/',user_views.user_register,name='user-register'),

path('login/',user_views.user_login,name='user-login'),
        path('logout/',user_views.user_logout,name='user-logout'),
        path('user-dashboard/',user_views.user_dashboard,name='user-dashboard'),
       path('profile/', user_views.profile, name='profile'),
        path('password-reset/',auth_views.PasswordResetView.as_view(template_name="user/password_reset.html",
        success_url='/password-reset/done/',from_email=None,)
            ,name='password_reset'),
        path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name="user/password_reset_done.html"),name='password_reset_done'),
        path('password-reset/confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="user/password_reset_confirm.html"),name='password_reset_confirm'),
path(
    'password-reset/complete/',
    auth_views.PasswordResetCompleteView.as_view(template_name="user/password_reset_complete.html"),
    name='password_reset_complete'
),
]