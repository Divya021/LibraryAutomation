# Generated by Django 2.2.2 on 2019-11-12 06:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_auto_20191109_1440'),
    ]

    operations = [
        migrations.RenameField(
            model_name='placeorder',
            old_name='Expirydate',
            new_name='expirydate',
        ),
        migrations.RemoveField(
            model_name='placeorder',
            name='Issuedate',
        ),
        migrations.RemoveField(
            model_name='placeorder',
            name='Studentname',
        ),
        migrations.AddField(
            model_name='placeorder',
            name='issuedate',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='placeorder',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='library.Studentinfo'),
        ),
        migrations.AddField(
            model_name='studentinfo',
            name='book',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='library.Book'),
        ),
    ]
