# Generated by Django 3.1.7 on 2021-03-23 16:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0026_auto_20210324_0027'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='ArrivalDate',
        ),
        migrations.AlterField(
            model_name='product',
            name='ExpireDate',
            field=models.DateField(default=datetime.date.today),
        ),
    ]