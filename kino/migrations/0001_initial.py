# Generated by Django 3.0.3 on 2020-02-17 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SozMovie',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('original_title', models.CharField(max_length=255)),
                ('overview', models.CharField(max_length=1000)),
                ('budget', models.CharField(max_length=255)),
                ('popularity', models.CharField(max_length=255)),
                ('vote_average', models.CharField(max_length=255)),
                ('original_language', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'фильмы',
                'managed': True,
            },
        ),
    ]