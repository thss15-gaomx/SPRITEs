# Generated by Django 2.1 on 2018-08-27 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plana', '0002_auto_20180827_0006'),
    ]

    operations = [
        migrations.AddField(
            model_name='block',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]
