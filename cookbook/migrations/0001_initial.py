# Generated by Django 3.0.7 on 2021-06-13 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='IngredientMeasurement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cookbook.Ingredient')),
            ],
        ),
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit', models.CharField(max_length=250)),
                ('system', models.CharField(max_length=250)),
                ('value', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('instructions', models.TextField()),
                ('image', models.ImageField(upload_to='cookbook/images')),
                ('author', models.CharField(max_length=250)),
                ('public', models.BooleanField(default=False)),
                ('category', models.CharField(max_length=250)),
                ('difficulty', models.CharField(max_length=250)),
                ('ingredient_measurements', models.ManyToManyField(to='cookbook.IngredientMeasurement', verbose_name='list of ingredients')),
            ],
        ),
        migrations.AddField(
            model_name='ingredientmeasurement',
            name='measurement',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cookbook.Measurement'),
        ),
    ]
