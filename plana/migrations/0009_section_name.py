# Generated by Django 2.1 on 2018-09-04 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plana', '0008_auto_20180902_2329'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='name',
            field=models.CharField(default='', max_length=64),
        ),
    ]
