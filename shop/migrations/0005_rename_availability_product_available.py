# Generated by Django 3.2.5 on 2021-07-25 17:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20210721_2032'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='availability',
            new_name='available',
        ),
    ]
