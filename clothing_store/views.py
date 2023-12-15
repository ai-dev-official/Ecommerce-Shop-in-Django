from django.shortcuts import render

from shop.models import Product, Category


def home(request):
    products = Product.objects.filter(is_featured=True)
    featured_categories = Category.objects.all().order_by('-is_featured')[0:5]
    popular_products = Product.objects.all().order_by('visits')[0:5]
    recently_viewed_products = Product.objects.all().order_by(
        '-last_visit')[0:5]

    context = {
        'products': products,
        'featured_categories': featured_categories,
        'popular_products': popular_products,
        'recently_viewed_products': recently_viewed_products
    }

    return render(request, 'home.html', context)
