# Generated by Django 3.0.5 on 2022-07-08 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blood', '0006_feedback_mobile'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='Email',
            field=models.EmailField(default=0, max_length=30),
        ),
    ]
