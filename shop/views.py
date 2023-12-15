from uuid import UUID
from django.shortcuts import render, get_object_or_404, redirect
from cart.models import Cart
from order.models import Order
from .models import Category, Product, Review
from datetime import datetime
import random
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.shortcuts import get_object_or_404
from django.views.generic import ListView


def product_detail(request, category_slug, slug):
    product = get_object_or_404(Product, slug=slug)
    product.visits = product.visits + 1
    product.last_visit = datetime.now()
    product.save()

    if request.method == 'POST' and request.user.is_authenticated:
        stars = request.POST.get('stars', 3)
        comment = request.POST.get('content', '')

        review = Review.objects.create(
            product=product, user=request.user, stars=stars, comment=comment)

        return redirect('product_detail', category_slug=category_slug, slug=slug)

    related_products = list(product.category.products.filter(
        parent=None).exclude(id=product.id))

    if len(related_products) >= 5:
        related_products = random.sample(related_products, 5)

    if product.parent:
        return redirect('product_detail', category_slug=category_slug, slug=product.parent.slug)

    context = {
        'product': product,
        'related_products': related_products
    }

    return render(request, 'product_detail.html', context)


def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = category.products.filter(parent=None)

    context = {
        'category': category,
        'products': products
    }

    return render(request, 'category_detail.html', context)



def review_rate(request):
    if request.method == "GET":
        prod_id = request.GET.get('prod_id')
        product = Product.objects.get(id=prod_id)
        comment = request.GET.get('comment')
        rate = request.GET.get('rate')
        user = request.user
        Review(user=user, product=product, comment=comment, rate=rate).save()
        return redirect('product_detail', id=prod_id)



class Shop__All__Products(ListView):
    model = Product

    def get(self, request, category_id=None):
        category = None
        products = None
        if category_id !=None:
            category = get_object_or_404(Category, id = category_id)
            products = Product.objects.filter(category = category, available=True)
        else:
            products = Product.objects.all().filter(available=True)

        ''' Pagination Code '''
        paginator = Paginator(products, 15)
        try:
            page = int(request.GET.get('page', '1'))
        except:
            page = 1
        try:
            products = paginator.page(page)
        except (EmptyPage, InvalidPage):
            products = paginator.page(paginator.num_pages)
        
        ''' End Pagination Code'''

        return render(request,"shop.html",{'category':category, 'products':products})   
