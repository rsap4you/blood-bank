# Generated by Django 3.0.5 on 2022-07-09 10:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0002_patient_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='bloodgroup',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='disease',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='doctorname',
        ),
    ]