
from django.contrib import admin
from django.urls import path,include
from admin_panel import views as admin_views

urlpatterns = [
    path('admin-panel/',admin_views.admin_login,name="admin-login"),
    path('admin-dashboard/',admin_views.admin_dashboard,name="admin-dashboard"),
    path('',include('products.urls')),
]
