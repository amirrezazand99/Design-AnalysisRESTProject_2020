# Generated by Django 2.1.7 on 2020-04-15 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_auto_20200414_1945'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]