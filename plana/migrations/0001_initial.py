# Generated by Django 2.1 on 2018-08-26 22:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pos_x', models.IntegerField(default=0)),
                ('pos_y', models.IntegerField(default=0)),
                ('width', models.IntegerField(default=1)),
                ('height', models.IntegerField(default=1)),
                ('color', models.CharField(default='#1b1c1d', max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Pic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.ImageField(upload_to='img')),
                ('name', models.CharField(default='anonymous', max_length=100)),
                ('block', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='plana.Block')),
            ],
        ),
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('font_size', models.IntegerField(blank=True, default=16)),
                ('font_color', models.CharField(default='white', max_length=64)),
                ('block', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='plana.Block')),
            ],
        ),
    ]
