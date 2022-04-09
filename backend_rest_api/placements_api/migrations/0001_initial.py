# Generated by Django 4.0.3 on 2022-04-09 15:50

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Placement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField()),
                ('name', models.CharField(max_length=155)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateField()),
                ('location', models.CharField(max_length=255)),
                ('foster_parents', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, size=None)),
                ('foster_siblings', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, size=None)),
                ('notes', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=500), blank=True, size=None)),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
