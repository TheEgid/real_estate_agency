# Generated by Django 2.2.6 on 2019-10-31 22:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0020_auto_20191030_0118'),
    ]

    operations = [
        migrations.RenameField(
            model_name='owner',
            old_name='flat',
            new_name='flats',
        ),
    ]