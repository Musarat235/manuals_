# Generated by Django 4.0.3 on 2022-08-25 17:51

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('manuals_app', '0002_remove_manual_pdf_end_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='manual_backend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=30)),
                ('Description', tinymce.models.HTMLField()),
                ('pdffile', models.FileField(default=None, max_length=250, null=True, upload_to='manuals/')),
            ],
            options={
                'db_table': 'manual_backend',
            },
        ),
        migrations.DeleteModel(
            name='manual_pdf',
        ),
    ]