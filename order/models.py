from django.utils import timezone
from django.db import models

from vendors.models import Vendor


class Order(models.Model):
    first_name = models.CharField(max_length=75, null=True, blank=True)
    last_name = models.CharField(max_length=75, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    place = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    paid_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    token = models.CharField(max_length=250, blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Order Total')
    emailAddress = models.EmailField(max_length=250, blank=True, verbose_name='Email Address')
    vendors = models.ForeignKey(
        Vendor, blank=True, null=True, related_name='orders', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    billingName = models.CharField(max_length=50, blank=True)
    billingAddress1 = models.CharField(max_length=100, blank=True)
    billingCity = models.CharField(max_length=25, blank=True)
    billingPostcode = models.CharField(max_length=10, blank=True)
    billingCountry = models.CharField(max_length=50, blank=True)
    shippingName = models.CharField(max_length=50, blank=True)
    shippingAddress1 = models.CharField(max_length=250, blank=True)
    shippingCity = models.CharField(max_length=25, blank=True)
    shippingPostcode = models.CharField(max_length=10, blank=True)
    shippingCountry = models.CharField(max_length=50, blank=True)

    class Meta:
        db_table = 'Order'
        ordering = ['-created']

    def __str__(self):
        return str(self.id)


class OrderItem(models.Model):
    ACCEPTED = "Accepted"
    ORDER_STATUS = (
    ("Accepted", 'Accepted'), ("Packed", 'Packed'), ("On The Way", 'On The Way'), ("Delivered", 'Delivered'),
    ("Cancel", 'Cancel'))
    product = models.CharField(max_length=50)
    size = models.CharField(max_length=50, default='', null=True)
    color = models.CharField(max_length=50, default='', null=True)
    status = models.CharField(max_length=15, choices=ORDER_STATUS, default=ACCEPTED)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Price')
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, related_name='items', on_delete=models.CASCADE)
    vendor_paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'OrderItem'

    def sub_total(self):
        return self.quantity * self.price

    def __str__(self):
        return self.product
