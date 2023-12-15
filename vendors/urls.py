from django.urls import path
from django.contrib.auth import views as auth_views
from .import views

app_name = 'vendors'

urlpatterns = [
    path('new_vendor', views.new_vendor, name="new_vendor"),
    path('vendor_admin/', views.vendors_admin, name='vendor_admin'),
    path('add_product/', views.add_product, name='add_product'),
    path('edit-vendor/', views.edit_vendor, name='edit_vendor'),
    path('edit-product/<str:pk>/', views.edit_product, name='edit_product'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='vendor/login.html'), name='login'),
    path('', views.vendors, name='vendors'),
    path('<int:vendor_id>/', views.vendor, name='vendor'),
]
