# Generated by Django 3.2.5 on 2021-08-22 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_SprMkt_Mgmt', '0003_alter_unitsconvertion_unit_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unitsconvertion',
            name='unit_type',
            field=models.CharField(choices=[('custom', 'Informal por convención entre usuarios'), ('SI', 'Sistema Internacional de Unidades')], max_length=50),
        ),
    ]