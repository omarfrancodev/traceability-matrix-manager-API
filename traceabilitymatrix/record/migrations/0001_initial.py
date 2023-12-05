# Generated by Django 4.2.7 on 2023-12-05 19:11

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
                ('projectRecordId', models.CharField(blank=True, max_length=255)),
                ('sprint', models.CharField(max_length=255)),
                ('phase', models.CharField(choices=[('Approval', 'Approval'), ('Initiation', 'Initiation'), ('Development', 'Development')], max_length=25)),
                ('type', models.CharField(max_length=255)),
                ('artifactName', models.CharField(max_length=255)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('keyRelationship', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('Proposed', 'Proposed'), ('Implemented', 'Implemented'), ('Verifying', 'Verifying'), ('Approved', 'Approved')], max_length=25)),
                ('createdAt', models.DateField(auto_now_add=True)),
                ('updatedAt', models.DateField(auto_now=True)),
                ('impact', models.CharField(choices=[('NA', 'NA'), ('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')], max_length=25)),
                ('notes', models.TextField(blank=True)),
                ('associatedProject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='associatedRecords', to='project.project')),
            ],
        ),
        migrations.CreateModel(
            name='ResourceURL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(blank=True, null=True)),
                ('record', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='urls', to='record.record')),
            ],
        ),
        migrations.CreateModel(
            name='ResourceFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, null=True, upload_to='files/')),
                ('record', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='files', to='record.record')),
            ],
        ),
    ]
