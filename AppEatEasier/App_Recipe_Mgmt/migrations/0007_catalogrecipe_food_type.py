# Generated by Django 3.2.5 on 2021-09-12 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Recipe_Mgmt', '0006_alter_recipeprocedure_pic_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='catalogrecipe',
            name='food_type',
            field=models.CharField(choices=[('res', 'Res'), ('pollo', 'Pollo'), ('cerdo', 'Cerdo'), ('pescado', 'Pescado'), ('huevo', 'Huevo'), ('lacteos', 'Lacteos'), ('frutas', 'Frutas'), ('verduras', 'Verduras'), ('gluten', 'Gluten')], default='pescado', max_length=30),
            preserve_default=False,
        ),
    ]
