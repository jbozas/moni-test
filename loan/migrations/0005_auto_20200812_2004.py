# Generated by Django 3.0.8 on 2020-08-12 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0004_auto_20200812_2001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='approved',
            field=models.BooleanField(),
        ),
    ]
