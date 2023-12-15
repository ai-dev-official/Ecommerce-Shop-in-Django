# Generated by Django 4.0.3 on 2022-04-22 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0008_order_paid_amount_order_phone_order_place'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='status',
            field=models.CharField(choices=[('Accepted', 'Accepted'), ('Packed', 'Packed'), ('On The Way', 'On The Way'), ('Delivered', 'Delivered'), ('Cancel', 'Cancel')], default='Accepted', max_length=15),
        ),
    ]
