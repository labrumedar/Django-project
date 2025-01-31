# Generated by Django 5.1.4 on 2025-01-13 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_demandstatistics'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='demandstatistics',
            name='vacancy_graph_image',
        ),
        migrations.RemoveField(
            model_name='demandstatistics',
            name='vacancy_html_table',
        ),
        migrations.AlterField(
            model_name='demandstatistics',
            name='graph_image',
            field=models.ImageField(blank=True, null=True, upload_to='graphs/', verbose_name='График (PNG)'),
        ),
        migrations.AlterField(
            model_name='demandstatistics',
            name='html_table',
            field=models.TextField(verbose_name='HTML таблица'),
        ),
    ]
