# Generated by Django 3.1.7 on 2021-04-01 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0035_color_color_square_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='color',
            name='color_square_url',
        ),
    ]
