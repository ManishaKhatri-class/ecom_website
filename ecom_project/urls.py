
from django.contrib import admin
from django.urls import path,include
from admin_panel import views as admin_views
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import RedirectView

  


urlpatterns = [
 path('home/',admin_views.home,name="home"),
    path('admin-panel/',admin_views.admin_login,name="admin-login"),
      path('admin-panel/logout',admin_views.admin_logout,name="admin-logout"),
    path('admin-dashboard/',admin_views.admin_dashboard,name="admin-dashboard"),
    path('',include('products.urls')),
     path('',include('user.urls')),
 path('',RedirectView.as_view(url='/home/',permanent=True)),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)



