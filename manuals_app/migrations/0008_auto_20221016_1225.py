# Generated by Django 3.1 on 2022-10-16 07:25

from django.db import migrations, models
import manuals_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('manuals_app', '0007_alter_category_parent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manual',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('pdf', models.FileField(blank=True, null=True, upload_to='pdf', validators=[manuals_app.models.validate_file_extension])),
                ('img', models.ImageField(blank=True, null=True, upload_to='img')),
            ],
        ),
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='manual_backend',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]