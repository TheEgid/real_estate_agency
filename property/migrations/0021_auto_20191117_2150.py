# Generated by Django 2.2.7 on 2019-11-17 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0020_auto_20191117_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='flats',
            field=models.ManyToManyField(blank=True, db_index=True, related_name='flats_owners', to='property.Flat', verbose_name='Квартиры в собственности'),
        ),
    ]
