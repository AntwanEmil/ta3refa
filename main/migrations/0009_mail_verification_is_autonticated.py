# Generated by Django 3.0.8 on 2021-01-09 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_mail_verification'),
    ]

    operations = [
        migrations.AddField(
            model_name='mail_verification',
            name='is_autonticated',
            field=models.BooleanField(default=False),
        ),
    ]
