# Generated by Django 4.2.6 on 2024-06-09 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_alter_orderdetail_size_alter_shopingcart_size_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='memberdata',
            name='address',
            field=models.CharField(default='', max_length=20, verbose_name='地址'),
        ),
    ]
