# Generated by Django 2.1.7 on 2020-04-16 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_auto_20200416_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrow_book',
            name='EndBorrowingTime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='borrow_book',
            name='StartBorrowingTime',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
