# Generated by Django 2.2.4 on 2019-08-08 21:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_auto_20190730_0043'),
        ('blog', '0005_auto_20190805_1838'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='project',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='project.Projects'),
            preserve_default=False,
        ),
    ]