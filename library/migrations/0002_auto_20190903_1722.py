# Generated by Django 2.2.2 on 2019-09-03 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Addbook',
            new_name='Book',
        ),
    ]
