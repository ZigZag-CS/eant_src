# Generated by Django 3.0.7 on 2020-06-11 09:55

import apps.products.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=apps.products.models.upload_image_path),
        ),
    ]
