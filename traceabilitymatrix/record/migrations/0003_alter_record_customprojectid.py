# Generated by Django 4.2.7 on 2023-11-29 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0002_rename_artifact_name_record_artifactname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='customProjectId',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]