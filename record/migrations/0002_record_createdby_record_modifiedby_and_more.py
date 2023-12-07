# Generated by Django 4.2.7 on 2023-12-07 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='createdBy',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='record',
            name='modifiedBy',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='record',
            name='createdAt',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='updatedAt',
            field=models.DateTimeField(auto_now=True),
        ),
    ]