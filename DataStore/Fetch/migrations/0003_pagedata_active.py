# Generated by Django 4.1.5 on 2023-01-11 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Fetch', '0002_remove_pagedata_updated_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagedata',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
