# Generated by Django 4.0.3 on 2022-04-11 11:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0011_remove_vendor_order_mycart'),
        ('order', '0003_order_vendor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='vendor',
            new_name='vendors',
        ),
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='first_name',
            field=models.CharField(blank=True, max_length=75, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='last_name',
            field=models.CharField(blank=True, max_length=75, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='paid_amount',
            field=models.DecimalField(decimal_places=2, default=0.00, max_digits=8),
        ),
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='place',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='vendor',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='vendors.vendor'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderitem',
            name='vendor_paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='billingAddress1',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='billingCity',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AlterField(
            model_name='order',
            name='billingCountry',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='billingName',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='shippingCity',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AlterField(
            model_name='order',
            name='shippingCountry',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='shippingName',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='product',
            field=models.CharField(max_length=50),
        ),
    ]
