# Generated by Django 4.1.1 on 2022-11-30 20:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articles',
            old_name='body',
            new_name='post',
        ),
    ]