import uuid
from django.conf import settings
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone
from vendors.models import Vendor
from vouchers.models import Voucher
from io import BytesIO
from PIL import Image
from django.core.files import File
from django.utils.text import slugify 


class Category(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    parent = models.ForeignKey(
        'self', related_name='children', on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(default="", max_length=255)
    ordering = models.IntegerField(default=0)
    is_featured = models.BooleanField(default=False)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'categories'
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/%s/' % (self.slug)


class Product(models.Model):
    MEDIUM = "M"
    YELLOW = "Yellow"
    COLOR = (("Yellow", 'Yellow'), ("Red", 'Red'), ("Green", 'Green'), ("Orange", 'Orange'), ("Black", 'Black'))
    SIZE = (("XL", 'XL'), ("L", 'L'), ("M", 'M'), ("S", 'S'), ("XS", 'XS'))
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    category = models.ForeignKey(
        Category, related_name='products', on_delete=models.CASCADE)
    vendor = models.ForeignKey(
        Vendor, blank=True, null=True, related_name='products', on_delete=models.CASCADE)
    parent = models.ForeignKey(
        'self', related_name='variants', on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    image1 = models.ImageField(upload_to='uploads/', blank=True, null=True)
    image2 = models.ImageField(upload_to='uploads/', blank=True, null=True)
    image3 = models.ImageField(upload_to='uploads/', blank=True, null=True)
    width = models.FloatField(default=300)
    length = models.FloatField(default=300)
    stock = models.IntegerField()
    size = models.CharField(max_length=6,choices=SIZE,default=MEDIUM, null=True)
    color = models.CharField(max_length=20,choices=COLOR,default=YELLOW, null=True)
    available = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    slug = models.SlugField(default="", max_length=255)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(default=timezone.now)
    visits = models.IntegerField(default=0)
    last_visit = models.DateTimeField(blank=True, null=True)
    voucher = models.ForeignKey(
        Voucher, default='', blank=True, null=True, on_delete=models.CASCADE)
    users_wishlist = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='user_wishlist', blank=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'product'
        verbose_name_plural = 'products'
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/%s/%s/' % (self.category.slug, self.slug)


class Review(models.Model):
    user = models.ForeignKey(
        User, related_name='review',  on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, related_name='review', on_delete=models.CASCADE)
    comment = models.TextField(max_length=250, blank=True, null=True)
    stars = models.IntegerField(default=0)
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.id)
