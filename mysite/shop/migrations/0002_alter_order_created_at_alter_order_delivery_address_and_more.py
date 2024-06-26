# Generated by Django 5.0.4 on 2024-04-23 08:47

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='created_at',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='created_at'),
        ),
        migrations.AlterField(
            model_name='order',
            name='delivery_address',
            field=models.CharField(max_length=50, verbose_name='delivery_address'),
        ),
        migrations.AlterField(
            model_name='order',
            name='promocode',
            field=models.CharField(default='', max_length=10, verbose_name='promocode'),
        ),
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='created_at'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(max_length=500, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.IntegerField(default=0, verbose_name='discount'),
        ),
        migrations.AlterField(
            model_name='product',
            name='is_archived',
            field=models.BooleanField(default=False, verbose_name='is_archived'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=50, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=8, verbose_name='price'),
        ),
    ]
