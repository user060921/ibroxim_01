# Generated by Django 4.1.7 on 2023-02-23 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loyiha_list', '0002_aboutadmissionwhyus_delete_about_delete_admission_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.CharField(blank=True, max_length=255, null=True)),
                ('twitter', models.CharField(blank=True, max_length=255, null=True)),
                ('linkenid', models.CharField(blank=True, max_length=255, null=True)),
                ('instagram', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
