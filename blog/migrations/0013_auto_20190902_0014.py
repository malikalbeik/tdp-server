# Generated by Django 2.2.4 on 2019-09-02 00:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_merge_20190901_2359'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-is_published', '-date_published', '-date_created'], 'permissions': [('can_change_post_is_published', 'Can change the publish status of the post')]},
        ),
    ]