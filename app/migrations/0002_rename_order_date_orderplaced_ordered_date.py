# Generated by Django 3.2.5 on 2021-07-10 05:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderplaced',
            old_name='order_date',
            new_name='ordered_date',
        ),
    ]
