# Generated by Django 2.2.2 on 2019-09-02 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Addbook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookid', models.IntegerField(null=True)),
                ('title', models.CharField(max_length=100, null=True)),
                ('Authorname', models.CharField(max_length=50, null=True)),
                ('cast', models.IntegerField(null=True)),
            ],
        ),
    ]
