# Generated by Django 2.1.7 on 2020-07-02 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='main_product/'),
        ),
    ]