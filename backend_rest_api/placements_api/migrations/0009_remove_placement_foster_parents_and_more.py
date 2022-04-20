# Generated by Django 4.0.3 on 2022-04-20 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('placements_api', '0008_placement_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='placement',
            name='foster_parents',
        ),
        migrations.RemoveField(
            model_name='placement',
            name='foster_siblings',
        ),
        migrations.CreateModel(
            name='FosterParent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=55)),
                ('last_name', models.CharField(max_length=55, null=True)),
                ('url', models.URLField(max_length=255)),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
                ('placement', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='placements_api.placement')),
            ],
        ),
    ]
