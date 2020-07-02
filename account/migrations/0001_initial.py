# Generated by Django 3.0.7 on 2020-07-01 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Observation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('station', models.CharField(max_length=255, null=True)),
                ('max_temp', models.CharField(max_length=255, null=True)),
                ('mini_temp', models.CharField(max_length=255, null=True)),
                ('rainfall_mm', models.FloatField(max_length=255, null=True)),
                ('status', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('stock', models.CharField(max_length=30)),
                ('price', models.CharField(max_length=60)),
                ('ratings', models.CharField(max_length=2)),
            ],
        ),
    ]
