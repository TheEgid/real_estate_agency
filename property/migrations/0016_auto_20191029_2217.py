# Generated by Django 2.2.6 on 2019-10-29 19:17

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0015_owner_data_migrate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='liked_by',
            field=models.ManyToManyField(blank=True, db_index=True, null=True, related_name='liked_flat', to=settings.AUTH_USER_MODEL, verbose_name='Кто лайкнул'),
        ),
        migrations.AlterField(
            model_name='owner',
            name='flat',
            field=models.ManyToManyField(db_index=True, related_name='owners_flats', to='property.Flat', verbose_name='Квартиры в собственности'),
        ),
    ]