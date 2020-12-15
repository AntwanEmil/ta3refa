# Generated by Django 3.1.2 on 2020-12-15 21:48

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20201211_1731'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('rated_products', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), size=None)),
                ('commented_products', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), size=None)),
            ],
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('shop_name', models.CharField(max_length=100)),
                ('telephone', models.IntegerField()),
                ('owned_products', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), size=None)),
            ],
        ),
        migrations.RenameField(
            model_name='person',
            old_name='first_name',
            new_name='username',
        ),
        migrations.RemoveField(
            model_name='person',
            name='email',
        ),
        migrations.RemoveField(
            model_name='person',
            name='last_name',
        ),
    ]
