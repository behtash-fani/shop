# Generated by Django 3.2.5 on 2021-09-13 11:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0018_product_details'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='details',
            new_name='specifications',
        ),
    ]
