# Generated by Django 3.0.5 on 2022-07-12 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0002_auto_20210213_1602'),
    ]

    operations = [
        migrations.AddField(
            model_name='donor',
            name='Email',
            field=models.EmailField(default=0, max_length=20),
        ),
    ]