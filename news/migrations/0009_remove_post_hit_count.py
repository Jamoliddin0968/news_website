# Generated by Django 4.1.5 on 2023-01-11 05:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_post_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='hit_count',
        ),
    ]
