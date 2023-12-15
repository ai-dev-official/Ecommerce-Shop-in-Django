from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Profile


class ProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        self.fields['image'].widget.attrs['class'] = 'input'
        self.fields['phone'].widget.attrs['class'] = 'input'
        self.fields['dob'].widget.attrs['class'] = 'input'
        self.fields['description'].widget.attrs['class'] = 'input'
        self.fields['gender'].widget.attrs['class'] = 'input'
        self.fields['address'].widget.attrs['class'] = 'input'
        self.fields['eircode'].widget.attrs['class'] = 'input'
        self.fields['city'].widget.attrs['class'] = 'input'
        self.fields['county'].widget.attrs['class'] = 'input'

    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ('user', 'date_created', 'date_updated')


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(max_length=255, required=True)

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'input'
        self.fields['first_name'].widget.attrs['class'] = 'input'
        self.fields['last_name'].widget.attrs['class'] = 'input'
        self.fields['email'].widget.attrs['class'] = 'input'
        self.fields['password1'].widget.attrs['class'] = 'input'
        self.fields['password2'].widget.attrs['class'] = 'input'

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email', 'password1', 'password2']



class ContactForm(forms.Form):
	first_name = forms.CharField(max_length = 25)
	last_name = forms.CharField(max_length = 25)
	email_address = forms.EmailField(max_length = 50)
	message = forms.CharField(widget = forms.Textarea, max_length = 1000)