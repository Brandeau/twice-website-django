# Generated by Django 5.1.6 on 2025-02-25 13:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groupings', '0001_initial'),
        ('releases', '0006_rename_release_group_id_release_release_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='releasegroup',
            name='groupings',
        ),
        migrations.AddField(
            model_name='releasegroup',
            name='grouping',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='grouping_of_release_group', to='groupings.grouping'),
        ),
    ]
