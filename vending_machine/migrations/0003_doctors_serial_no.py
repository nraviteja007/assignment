# Generated by Django 4.1.5 on 2023-01-14 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vending_machine', '0002_alter_departments_options_alter_doctors_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctors',
            name='serial_no',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]
