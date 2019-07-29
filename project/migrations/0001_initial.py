# Generated by Django 2.2.3 on 2019-07-26 00:50

from django.db import migrations, models
import project.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('shortDescription', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('logo', models.ImageField(blank=True, upload_to=project.models.get_image_path)),
                ('backgroundImage', models.ImageField(blank=True, upload_to=project.models.get_image_path)),
            ],
        ),
    ]