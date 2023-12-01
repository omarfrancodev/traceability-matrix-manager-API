# Generated by Django 4.2.7 on 2023-11-30 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0008_alter_record_locationresources_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='locationResources',
            field=models.ManyToManyField(blank=True, related_name='recordLocationResources', to='record.locationresource'),
        ),
        migrations.AlterField(
            model_name='record',
            name='urlResources',
            field=models.ManyToManyField(blank=True, related_name='recordUrlsResources', to='record.urlresource'),
        ),
    ]
