# Generated by Django 4.0.3 on 2022-04-10 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0009_remove_vendor_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='last_login',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
