# Generated by Django 3.2.4 on 2021-12-25 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='desc',
            field=models.CharField(default='', max_length=100),
        ),
    ]
