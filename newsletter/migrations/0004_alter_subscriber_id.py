# Generated by Django 4.0.3 on 2022-04-17 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0003_alter_subscriber_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriber',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
