# Generated by Django 4.0.3 on 2022-10-07 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manuals_app', '0004_alter_manual_backend_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manual_backend',
            name='Description',
            field=models.TextField(),
        ),
    ]
