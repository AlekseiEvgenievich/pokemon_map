# Generated by Django 3.1.14 on 2024-01-15 15:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0005_auto_20240115_1128'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pokemon',
            name='parent',
        ),
        migrations.AddField(
            model_name='pokemon',
            name='previous_evolution',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='next_evolution', to='pokemon_entities.pokemon', verbose_name='имя родителя'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='photo',
            field=models.ImageField(upload_to='', verbose_name='фото покемона'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='title',
            field=models.CharField(max_length=64, verbose_name='имя покемона'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='title_en',
            field=models.CharField(blank=True, max_length=64, verbose_name='имя покемона на английском'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='title_jp',
            field=models.CharField(blank=True, max_length=64, verbose_name='имя покемона на японском'),
        ),
    ]
