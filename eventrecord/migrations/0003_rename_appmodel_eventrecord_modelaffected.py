# Generated by Django 4.2.7 on 2023-12-09 19:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventrecord', '0002_remove_eventrecord_userfullnameaffected_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eventrecord',
            old_name='appModel',
            new_name='modelAffected',
        ),
    ]
