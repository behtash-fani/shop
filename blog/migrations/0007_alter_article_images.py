# Generated by Django 3.2.5 on 2021-09-17 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_article_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='blog_images/%Y/%m/%d/'),
        ),
    ]
