# Generated by Django 4.0.3 on 2022-04-12 00:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('placements_api', '0002_placement_test_field'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='placement',
            name='test_field',
        ),
    ]
