# Generated by Django 4.2.7 on 2023-11-30 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0004_alter_record_locationresource'),
    ]

    operations = [
        migrations.RenameField(
            model_name='record',
            old_name='customProjectId',
            new_name='projectRecordId',
        ),
    ]