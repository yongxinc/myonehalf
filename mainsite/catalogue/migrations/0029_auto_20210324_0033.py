# Generated by Django 3.1.7 on 2021-03-23 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0028_product_arrivaldate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='ArrivalDate',
        ),
        migrations.RemoveField(
            model_name='product',
            name='ExpireDate',
        ),
        migrations.RemoveField(
            model_name='product',
            name='ExtendTimes',
        ),
    ]
