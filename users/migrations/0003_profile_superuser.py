# Generated by Django 3.0.8 on 2020-08-14 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200812_2001'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='superuser',
            field=models.BooleanField(default=False),
        ),
    ]