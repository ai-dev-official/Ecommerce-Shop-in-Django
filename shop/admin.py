from django.contrib import admin
from .models import Category, Product, Review


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'description',
                    'category', 'stock', 'available', 'created', 'updated', 'voucher', ]
    list_editable = ['price', 'stock', 'available']
    list_per_page = 20


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product', 'stars', 'date_added', ]
    readonly_fields = ['date_added', ]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
