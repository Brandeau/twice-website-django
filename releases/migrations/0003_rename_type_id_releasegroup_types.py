# Generated by Django 5.1.6 on 2025-02-25 13:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('releases', '0002_remove_releasegroup_grouping_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='releasegroup',
            old_name='type_id',
            new_name='types',
        ),
    ]
