# Generated by Django 2.2.4 on 2019-08-04 16:33

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content',
            field=ckeditor.fields.RichTextField(default='test'),
            preserve_default=False,
        ),
    ]
