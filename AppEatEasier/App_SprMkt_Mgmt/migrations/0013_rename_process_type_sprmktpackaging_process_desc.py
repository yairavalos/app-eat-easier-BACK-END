# Generated by Django 3.2.5 on 2021-08-23 03:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App_SprMkt_Mgmt', '0012_alter_catalogpackage_container_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sprmktpackaging',
            old_name='process_type',
            new_name='process_desc',
        ),
    ]