# Generated by Django 4.1.1 on 2022-10-04 20:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0013_rename_address_destination_city'),
    ]

    operations = [
        migrations.RenameField(
            model_name='destination',
            old_name='city',
            new_name='address',
        ),
    ]