from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import login
from django.urls import reverse_lazy
from accounts.forms import ProfileForm, SignUpForm
from django.utils import timezone
from accounts.models import Profile
from django.contrib.auth.models import User
from order.models import Order
from vendors.forms import ProductForm, VendorCreationForm
from django.utils.text import slugify
from .models import MyCart, Vendor
from shop.models import Product
from django.contrib.auth.decorators import login_required
from django.contrib import messages



@login_required
def new_vendor(request):
    if request.method == 'POST':
        form = VendorCreationForm(request.POST)
        if form.is_valid():
            
            usr=request.user
            user = form.save()
            login(request, user)
        
            vendor = Vendor.objects.create(user=usr, is_vendor=True)
            return redirect('vendors:vendor_admin')
    else:
        form = VendorCreationForm()

    return render(request, 'vendor/new_vendor.html', {'form': form})



@login_required
def vendors_admin(request):
    vendor = request.user.vendor
    products = vendor.products.all()
    orders = vendor.orders.all()

    for order in orders:
        order.vendor_amount = 0
        order.vendor_paid_amount = 0
        order.fully_paid = True

        for item in order.items.all():
            if item.vendor == request.user.vendor:
                if item.vendor_paid:
                    order.vendor_paid_amount += item.get_total_price()
                else:
                    order.vendor_amount += item.get_total_price()
                    order.fully_paid = False

    return render(request, 'vendor/vendor_admin.html', {'vendor': vendor, 'products': products, 'orders': orders})


@login_required
def add_product(request):
    form_class = ProductForm
    form = form_class(request.POST or None)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)

    if form.is_valid():
        product = form.save(commit=False)
        product.vendor = request.user.vendor
        product.slug = slugify(product.name)
        product.save()

        return redirect('vendors:vendor_admin')
    else:
        form = ProductForm()

    return render(request, 'vendor/add_product.html', {'form': form})



# Vendor Cart
@login_required
def mycart(request):
    if request.user.is_superuser or request.user.is_staff:
        allProds = []
        subtotal = 0.0
        delev = 0.0
        cart_prods = [p for p in MyCart.objects.all() if p.user == request.user]
        for p in cart_prods:
            subtotal += p.number * Product.objects.filter(product_id=p.product_id)[0].price
        tax = subtotal*0.05

        for cprod in cart_prods:
            prod = Product.objects.filter(product_id=cprod.product_id)[0]
            allProds.append([cprod, prod])
        params = {
                    'allProds':allProds,
                    'cart_element_no' : len([p for p in MyCart.objects.all() if p.user == request.user]),
                    'total':subtotal+tax+delev,
                    'subtotal':subtotal,
                    'tax':tax,
                    'delev':delev,
                }
        return render(request,'vendor/cart.html', params)
    else:
        return redirect("/")



def MyOrders(request):
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        o = Order.objects.filter(order_id=order_id)[0]
        o.status = 'Cancel'
        o.save()
    params = {
        'orders': [i for i in Order.objects.all() if i.user == request.user and i.status != 'Delivered' and i.status != 'Cancel'],
        'delivered': [i for i in Order.objects.all() if i.user == request.user and i.status == 'Delivered'],
        'cancel': [i for i in Order.objects.all() if i.user == request.user and i.status == 'Cancel'],

    }
    return render(request,'vendor/myorders.html', params)



@login_required
def edit_product(request, pk):
    vendor = request.user.vendor
    product = vendor.products.get(pk=pk)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)

        if form.is_valid():
            form.save()

            return redirect('vendors:vendor_admin')
    else:
        form = ProductForm(instance=product)
       
    
    return render(request, 'vendor/edit_product.html', {'form': form, 'product': product})

@login_required
def edit_vendor(request):
    vendor = request.user.vendor

    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')

        if name:
            vendor.created_by.email = email
            vendor.created_by.save()

            vendor.name = name
            vendor.save()

            return redirect('vendors:vendor_admin')
    
    return render(request, 'vendor/edit_vendor.html', {'vendor': vendor})

def vendors(request):
    vendors = Vendor.objects.all()

    return render(request, 'vendor/vendors.html', {'vendors': vendors})

def vendor(request, vendor_id):
    vendor = get_object_or_404(Vendor, pk=vendor_id)

    return render(request, 'vendor/vendor.html', {'vendor': vendor})