from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from django.core.mail import send_mail, BadHeaderError
from shop.models import Product
from .models import Profile
from .forms import ContactForm, SignUpForm, ProfileForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        profileform = ProfileForm(request.POST)

        if form.is_valid() and profileform.is_valid():
            user = form.save()

            accounts = profileform.save(commit=False)
            accounts.user = user
            accounts.save()

            login(request, user)

            return redirect('/')
    else:
        form = SignUpForm()
        profileform = ProfileForm()

    return render(request, 'registration/signup.html', {'form': form, 'profileform': profileform})


@login_required
def myprofile(request):
    return render(request, 'registration/profile.html')


class UserEditView(UpdateView):
    model = Profile
    template_name = 'registration/edit_profile.html'
    fields = '__all__'
    success_url = reverse_lazy('login')

    def get_object(self):
        return self.request.user.profile


@login_required
def wishlist(request):
    products = Product.objects.filter(users_wishlist=request.user)
    wishlist_count = Product.objects.filter(users_wishlist=request.user).count()
    context = {
        'wishlist_count': wishlist_count,
        'wishlist': products
    }
    return render(request, "registration/wishlist.html", context)


@login_required
def add_to_wishlist(request, id):
    product = get_object_or_404(Product, id=id)
    wishlist_count = Product.objects.count()
    if product.users_wishlist.filter(id=request.user.id).exists():
        product.users_wishlist.remove(request.user)
        wishlist_count -= wishlist_count
    else:
        product.users_wishlist.add(request.user)
        wishlist_count += wishlist_count
    return HttpResponseRedirect(request.META["HTTP_REFERER"])




def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = "Customer Service" 
			body = {
			'first_name': form.cleaned_data['first_name'], 
			'last_name': form.cleaned_data['last_name'], 
			'email': form.cleaned_data['email_address'], 
			'message':form.cleaned_data['message'], 
			}
			message = "\n".join(body.values())

			try:
				send_mail(subject, message, 'admin@admin.com', ['admin@admin.com']) 
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return redirect ("/")
      
	form = ContactForm()
	return render(request, "registration/customer__service.html", {'form':form})