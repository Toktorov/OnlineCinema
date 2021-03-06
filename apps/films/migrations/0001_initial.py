# Generated by Django 3.2.7 on 2021-11-15 12:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_created=True)),
                ('title', models.CharField(max_length=100, verbose_name='Название фильма')),
                ('description', models.TextField(verbose_name='Описание фильма')),
                ('year', models.PositiveIntegerField(verbose_name='Год выпуска')),
                ('country', models.CharField(max_length=100, verbose_name='Страна')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='FilmImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='film', verbose_name='Фотография фильма')),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='film_image', to='films.film')),
            ],
        ),
    ]
