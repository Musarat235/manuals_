# Generated by Django 4.0.3 on 2022-08-24 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='manual_pdf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=30)),
                ('Description', models.CharField(max_length=200)),
                ('Download', models.CharField(max_length=300)),
                ('Start_Date', models.DateField()),
                ('End_Date', models.DateField()),
            ],
            options={
                'db_table': 'manual_pdf',
            },
        ),
    ]
