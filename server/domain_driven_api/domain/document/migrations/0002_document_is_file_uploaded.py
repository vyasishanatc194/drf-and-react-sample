# Generated by Django 4.2.7 on 2023-12-05 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='is_file_uploaded',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
