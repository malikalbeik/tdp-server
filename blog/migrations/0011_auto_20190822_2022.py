# Generated by Django 2.2.4 on 2019-08-22 20:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20190813_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='project',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='project.Projects'),
            preserve_default=False,
        ),
    ]
