# Generated by Django 3.2.5 on 2021-08-22 22:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App_SprMkt_Mgmt', '0004_alter_unitsconvertion_unit_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='catalogingredient',
            name='ingredient_cal',
        ),
    ]
