# Generated by Django 3.2.5 on 2021-09-16 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210916_2322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='status',
            field=models.CharField(choices=[('d', 'Draft'), ('p', 'Published')], max_length=1),
        ),
    ]