# Generated by Django 4.0.3 on 2022-04-13 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_product_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='thumbnail',
        ),
    ]
