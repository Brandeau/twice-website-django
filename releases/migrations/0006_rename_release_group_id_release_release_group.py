# Generated by Django 5.1.6 on 2025-02-25 13:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('releases', '0005_rename_country_id_release_country'),
    ]

    operations = [
        migrations.RenameField(
            model_name='release',
            old_name='release_group_id',
            new_name='release_group',
        ),
    ]
