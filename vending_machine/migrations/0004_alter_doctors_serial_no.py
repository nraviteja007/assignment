# Generated by Django 4.1.5 on 2023-01-14 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vending_machine', '0003_doctors_serial_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctors',
            name='serial_no',
            field=models.CharField(max_length=100),
        ),
    ]
