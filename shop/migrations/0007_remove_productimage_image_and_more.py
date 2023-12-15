# Generated by Django 4.0.2 on 2022-02-27 00:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_rename_thumbnail_productimage_image1_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productimage',
            name='image',
        ),
        migrations.RemoveField(
            model_name='productimage',
            name='product',
        ),
        migrations.AddField(
            model_name='product',
            name='length',
            field=models.FloatField(default=300),
        ),
        migrations.AddField(
            model_name='product',
            name='productimage',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='shop.productimage'),
        ),
        migrations.AddField(
            model_name='product',
            name='width',
            field=models.FloatField(default=300),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]