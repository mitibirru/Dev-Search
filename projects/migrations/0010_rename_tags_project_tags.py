# Generated by Django 3.2.6 on 2021-11-22 08:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_rename_tags_project_tags'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='tags',
            new_name='Tags',
        ),
    ]
