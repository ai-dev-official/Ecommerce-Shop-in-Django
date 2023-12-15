from . import views
from django.urls import path
from .views import UserEditView, myprofile, signup

app_name = 'accounts'

urlpatterns = [
    path('myprofile/', myprofile, name='myprofile'),
    path('signup/', signup, name='signup'),
    path("customer_service", views.contact, name="customer_service"),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    path("wishlist", views.wishlist, name="wishlist"),
    path('wishlist/add_to_wishlist/<str:id>',
         views.add_to_wishlist, name='user_wishlist'),
]
