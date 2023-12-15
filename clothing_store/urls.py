
from . import views
from newsletter.api import api_add_subscriber
from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from shop.views import product_detail, category_detail, review_rate, Shop__All__Products

urlpatterns = [
    path('', views.home),
    path('admin/', admin.site.urls),
    path('vendors/', include('vendors.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('search/', include('search_app.urls')),
    path('cart/', include('cart.urls')),
    path('order/', include('order.urls')),
    path('vouchers/', include('vouchers.urls')),
    path('review/', review_rate, name='review'),
    path('api/add_subscriber/', api_add_subscriber, name='api_add_subscriber'),


    # SHOP
    path('shop_products', Shop__All__Products.as_view(), name='shop_products'),

    # SHOP

    path('<slug:category_slug>/<slug:slug>/',
         product_detail, name='product_detail'),
    path('<slug:slug>/',
         category_detail, name='category_detail'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
