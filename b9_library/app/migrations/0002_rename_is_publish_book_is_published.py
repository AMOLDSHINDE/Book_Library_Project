# Generated by Django 4.2.1 on 2023-06-17 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='is_publish',
            new_name='is_published',
        ),
    ]
