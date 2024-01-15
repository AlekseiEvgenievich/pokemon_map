# Generated by Django 3.1.14 on 2024-01-15 00:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('title_en', models.TextField(default='Bulbausaur')),
                ('title_jp', models.TextField(default='フシギダネ')),
                ('photo', models.ImageField(blank=True, upload_to='')),
                ('description', models.TextField(default='hhhhh')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='evolutions', to='pokemon_entities.pokemon')),
            ],
        ),
        migrations.CreateModel(
            name='PokemonEntity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latttude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('appeared_at', models.DateTimeField(null=True)),
                ('disappeared_at', models.DateTimeField(null=True)),
                ('level', models.IntegerField(null=True)),
                ('health', models.IntegerField(null=True)),
                ('attack', models.IntegerField(null=True)),
                ('protection', models.IntegerField(null=True)),
                ('endurance', models.IntegerField(null=True)),
                ('pokemon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pokemon_entities.pokemon')),
            ],
        ),
    ]
