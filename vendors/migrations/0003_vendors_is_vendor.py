# Generated by Django 4.0.3 on 2022-03-17 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0002_rename_vendor_vendors'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendors',
            name='is_vendor',
            field=models.BooleanField(default=True),
        ),
    ]
