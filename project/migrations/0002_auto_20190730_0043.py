# Generated by Django 2.2.3 on 2019-07-30 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='instagramAccount',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='projects',
            name='twitterAccount',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
