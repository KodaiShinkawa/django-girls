# Generated by Django 3.0.4 on 2020-03-31 08:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='created_day',
            new_name='created_date',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='published_day',
            new_name='published_date',
        ),
    ]
