# Generated by Django 3.2.5 on 2021-09-17 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20210916_2338'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='images',
            field=models.ImageField(null=True, upload_to='blog_images/%Y/%m/%d/'),
        ),
    ]
