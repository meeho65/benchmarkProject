# Generated by Django 4.2.7 on 2024-01-01 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kleemoapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobileproducts',
            name='market_share',
            field=models.JSONField(),
        ),
    ]
