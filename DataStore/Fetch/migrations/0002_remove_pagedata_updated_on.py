# Generated by Django 4.1.5 on 2023-01-11 10:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Fetch', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pagedata',
            name='updated_on',
        ),
    ]