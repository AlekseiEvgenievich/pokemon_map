# Generated by Django 3.1.14 on 2024-01-12 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0002_pokemon_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='PokemonEntity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latttude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
        ),
    ]