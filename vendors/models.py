from datetime import timezone
from django.contrib.auth.models import User
from django.db import models



class Vendor(models.Model):
    DUBLIN = 'Dublin'
    MALE = 'Male'
    GENDER = (("Male", 'Male'), ("Female", 'Female'), ("Other", 'Other'))
    COUNTY = (
        ("Carlow", 'Carlow'),
        ("Cavan", 'Cavan'),
        ("Clare", 'Clare'),
        ("Cork", 'Cork'),
        ("Donegal", 'Donegal'),
        ("Dublin", 'Dublin'),
        ("Galway", 'Galway'),
        ("Kerry", 'Kerry'),
        ("Kildare", 'Kildare'),
        ("Kilkenny", 'Kilkenny'),
        ("Laois", 'Laois'),
        ("Leitrim", 'Leitrim'),
        ("Limerick", 'Limerick'),
        ("Longford", 'Longford'),
        ("Louth", 'Louth'),
        ("Mayo", 'Mayo'),
        ("Meath", 'Meath'),
        ("Monaghan", 'Monaghan'),
        ("Offaly", 'Offaly'),
        ("Roscommon", 'Roscommon'),
        ("Sligo", 'Sligo'),
        ("Tipperary", 'Tipperary'),
        ("Waterford", 'Waterford'),
        ("Westmeath", 'Westmeath'),
        ("Wexford", 'Wexford'),
        ("Wicklow", 'Wicklow'),
    )
    user = models.OneToOneField(
        User, null=True, on_delete=models.CASCADE,  related_name="vendor")
    is_vendor = models.BooleanField(default=True)
    is_approved = models.BooleanField(default=False)
    account_name = models.CharField(
        max_length=100, blank=True, null=True, default="")
    bank_IBAN = models.CharField(max_length=50, blank=True, null=True)
    bank_name = models.CharField(max_length=50, blank=True, null=True)
    bank_bic = models.CharField(max_length=25, blank=True, null=True)
    county = models.CharField(max_length=50,choices=COUNTY, default=DUBLIN, null=True)
    gender = models.CharField(max_length=6,choices=GENDER, default=MALE, null=True)
    created_at = models.DateField(auto_now=True)
    last_login = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at', ]

    def __str__(self):
        return str(self.user)

    def get_balance(self):
        items = self.items.filter(vendor_paid=False, order__vendors__in=[self.id])
        return sum((item.product.price * item.quantity) for item in items)
    
    def get_paid_amount(self):
        items = self.items.filter(vendor_paid=True, order__vendors__in=[self.id])

        return sum((item.product.price * item.quantity) for item in items)


class MyCart(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	product_id = models.CharField(max_length=100)
	number = models.PositiveIntegerField(default=0)