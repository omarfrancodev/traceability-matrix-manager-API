# Generated by Django 4.2.7 on 2023-11-29 18:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customProjectId', models.CharField(max_length=255)),
                ('sprint', models.CharField(max_length=255)),
                ('artifact_name', models.CharField(max_length=255)),
                ('urlResource', models.URLField(blank=True, null=True)),
                ('locationResource', models.FileField(blank=True, null=True, upload_to='media/')),
                ('keyRelationship', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=255)),
                ('responsible', models.CharField(max_length=255)),
                ('creationDate', models.DateField(auto_now_add=True)),
                ('updateDate', models.DateField(auto_now=True)),
                ('impact', models.CharField(max_length=255)),
                ('notes', models.TextField(blank=True)),
                ('associatedProject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='associatedRecords', to='project.project')),
            ],
        ),
    ]
