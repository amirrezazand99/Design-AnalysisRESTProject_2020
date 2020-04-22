# Generated by Django 2.1.7 on 2020-04-22 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0012_auto_20200421_2010'),
        ('cart', '0006_auto_20200422_1431'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='order_items',
        ),
        migrations.AddField(
            model_name='cart',
            name='order_items',
            field=models.ManyToManyField(related_name='Item_want_to_buy', to='books.Proposed_Book'),
        ),
    ]
