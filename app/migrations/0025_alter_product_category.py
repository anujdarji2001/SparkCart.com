# Generated by Django 3.2.5 on 2021-07-17 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('E', 'Electronics'), ('Mobile', 'Mobile'), ('L', 'Laptop'), ('C', 'Camera'), ('MTS', 'Mens Tshirt'), ('MS', 'Mens Shirt'), ('MJ', 'Mens Jeans'), ('MSU', 'Mens Suit'), ('MW', 'Mens Watch'), ('MSH', 'Mens Shoes'), ('WTS', 'Womens Tshirt'), ('WJ', 'Womens Jeans'), ('WT', 'Womens Tops'), ('WK', 'Womens Kurti'), ('WSA', 'Womens Saree'), ('WW', 'Womens Watch'), ('WSH', 'Womens Shoes')], max_length=7),
        ),
    ]
