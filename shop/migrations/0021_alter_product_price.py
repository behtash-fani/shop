# Generated by Django 3.2.5 on 2021-09-13 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0020_product_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
