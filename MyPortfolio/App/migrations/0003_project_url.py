# Generated by Django 4.1.5 on 2023-01-12 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_alter_project_description_alter_project_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='url',
            field=models.URLField(blank=True),
        ),
    ]
