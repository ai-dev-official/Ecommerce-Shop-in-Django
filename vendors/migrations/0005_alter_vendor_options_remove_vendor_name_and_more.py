# Generated by Django 4.0.3 on 2022-03-24 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0004_rename_vendors_vendor'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vendor',
            options={'ordering': ['-created_at']},
        ),
        migrations.RemoveField(
            model_name='vendor',
            name='name',
        ),
        migrations.AddField(
            model_name='vendor',
            name='account_name',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='vendor',
            name='bank_IBAN',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='vendor',
            name='bank_bic',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='vendor',
            name='bank_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
