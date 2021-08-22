# Generated by Django 3.2.5 on 2021-08-22 17:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('App_Recipe_Mgmt', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adults_qty', models.IntegerField()),
                ('child_qty', models.IntegerField()),
                ('my_user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='user_profiles', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserRecipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checked', models.BooleanField(default=False)),
                ('favorite', models.BooleanField(default=False)),
                ('cat_recipe', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user_recipes', to='App_Recipe_Mgmt.catalogrecipe')),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user_recipes', to='App_User_Mgmt.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='UserPlanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan_title', models.CharField(max_length=150, unique=True)),
                ('week_num', models.IntegerField()),
                ('period', models.CharField(choices=[('semanal', 'Semanal'), ('quincenal', 'Quincenal')], max_length=30)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('saved', models.BooleanField(default=False)),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user_planners', to='App_User_Mgmt.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='UserMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meal_date', models.DateField()),
                ('meal_type', models.CharField(choices=[('desayuno', 'Desayuno'), ('brunch', 'Brunch'), ('comida', 'Comida'), ('merienda', 'Merienda'), ('cena', 'Cena')], max_length=20)),
                ('done', models.BooleanField(default=False)),
                ('user_planner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user_menus', to='App_User_Mgmt.userplanner')),
                ('user_recipe', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user_menus', to='App_User_Mgmt.userrecipe')),
            ],
        ),
        migrations.CreateModel(
            name='UserFood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_type', models.CharField(choices=[('res', 'Res'), ('pollo', 'Pollo'), ('cerdo', 'Cerdo'), ('pescado', 'Pescado'), ('huevo', 'Huevo'), ('lacteos', 'Lacteos'), ('frutas', 'Frutas'), ('verduras', 'Verduras'), ('gluten', 'Gluten')], max_length=30)),
                ('my_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user_foods', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserApp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_name', models.CharField(choices=[('olla de presion', 'Olla de Presión'), ('licuadora', 'Licuadora'), ('microondas', 'Microondas'), ('horno', 'Horno'), ('procesador', 'Procesador'), ('estufa', 'Estufa')], max_length=30)),
                ('my_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user_apps', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]