# Generated by Django 4.0.3 on 2022-04-25 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0014_alter_vendor_county_alter_vendor_gender'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vendor',
            old_name='bank_name',
            new_name='bank_nam',
        ),
    ]