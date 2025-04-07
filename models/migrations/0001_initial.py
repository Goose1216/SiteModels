# Generated by Django 5.2 on 2025-04-07 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=255)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='models_upload/', verbose_name='Файл')),
                ('description', models.TextField(blank=True, max_length=500, null=True, verbose_name='Описание')),
                ('cnt_downloads', models.IntegerField(default=0, verbose_name='Количество загрузок')),
                ('cnt_likes', models.IntegerField(default=0, verbose_name='Количество лайков')),
            ],
        ),
    ]
