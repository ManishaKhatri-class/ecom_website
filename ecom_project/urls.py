
from django.contrib import admin
from django.urls import path,include
from admin_panel import views as admin_views
from django.conf.urls.static import static
from django.conf import settings
<<<<<<< HEAD
  


urlpatterns = [

    path('admin-panel/',admin_views.admin_login,name="admin-login"),
      path('admin-panel/logout',admin_views.admin_logout,name="admin-logout"),
    path('admin-dashboard/',admin_views.admin_dashboard,name="admin-dashboard"),
    path('',include('products.urls')),
     path('',include('user.urls')),
=======

  


urlpatterns = [

    path('admin-panel/',admin_views.admin_login,name="admin-login"),
      path('admin-panel/logout',admin_views.admin_logout,name="admin-logout"),
    path('admin-dashboard/',admin_views.admin_dashboard,name="admin-dashboard"),
    path('',include('products.urls')),
<<<<<<< HEAD
     path('',include('user.urls')),
=======
>>>>>>> 93a7b86ed4178619cc4bc13f8f0f6141663a87af
>>>>>>> cb1b3181f1be4f3ce5ea799625050162a878655a
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)



