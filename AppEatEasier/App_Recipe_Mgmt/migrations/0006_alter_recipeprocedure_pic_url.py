# Generated by Django 3.2.5 on 2021-08-23 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Recipe_Mgmt', '0005_rename_apps_main_recipeapp_required'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipeprocedure',
            name='pic_url',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]