# Generated by Django 4.2.7 on 2023-12-04 20:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_alter_user_role'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Guest',
        ),
        migrations.DeleteModel(
            name='TeamMember',
        ),
    ]