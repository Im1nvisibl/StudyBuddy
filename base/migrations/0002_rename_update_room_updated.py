# Generated by Django 4.0.1 on 2022-02-02 21:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='update',
            new_name='updated',
        ),
    ]