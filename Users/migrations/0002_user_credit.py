# Generated by Django 2.1.7 on 2020-05-18 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='credit',
            field=models.IntegerField(default=0),
        ),
    ]
