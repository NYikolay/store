# Generated by Django 3.2.4 on 2021-06-21 19:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20210619_1827'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcategory',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now, unique=True),
            preserve_default=False,
        ),
    ]