# Generated by Django 5.1.6 on 2025-02-25 13:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('releases', '0003_rename_type_id_releasegroup_types'),
    ]

    operations = [
        migrations.RenameField(
            model_name='release',
            old_name='format_id',
            new_name='format',
        ),
    ]
