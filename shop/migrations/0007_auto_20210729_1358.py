# Generated by Django 3.2.5 on 2021-07-29 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_alter_product_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='is_sub',
            new_name='is_main_category',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='sub_category',
            new_name='main_category',
        ),
        migrations.AddField(
            model_name='category',
            name='is_sub_category',
            field=models.BooleanField(default=False),
        ),
    ]
