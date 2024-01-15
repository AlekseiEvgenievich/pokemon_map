# Generated by Django 3.1.14 on 2024-01-15 11:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0003_auto_20240115_0038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='description',
            field=models.TextField(default='hhhhh', verbose_name='описание покемона'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='evolutions', to='pokemon_entities.pokemon', verbose_name='имя родителя'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='photo',
            field=models.ImageField(blank=True, upload_to='', verbose_name='фото покемона'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='title',
            field=models.TextField(verbose_name='имя покемона'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='title_en',
            field=models.TextField(default='Bulbausaur', verbose_name='имя покемона на английском'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='title_jp',
            field=models.TextField(default='フシギダネ', verbose_name='имя покемона на японском'),
        ),
    ]