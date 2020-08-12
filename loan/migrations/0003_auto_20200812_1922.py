# Generated by Django 3.0.8 on 2020-08-12 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0002_auto_20200812_1857'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserRegistered',
        ),
        migrations.RemoveField(
            model_name='loan',
            name='email',
        ),
        migrations.RemoveField(
            model_name='loan',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='loan',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='loan',
            name='last_name',
        ),
        migrations.AddField(
            model_name='loan',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
