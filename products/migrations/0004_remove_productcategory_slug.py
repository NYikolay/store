# Generated by Django 3.2.4 on 2021-06-21 19:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_productcategory_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productcategory',
            name='slug',
        ),
    ]
