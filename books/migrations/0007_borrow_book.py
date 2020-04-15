# Generated by Django 2.1.7 on 2020-04-15 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
        ('books', '0006_auto_20200415_1732'),
    ]

    operations = [
        migrations.CreateModel(
            name='Borrow_book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StartBorrowingTime', models.CharField(default='بدون زمان شروع ', max_length=100)),
                ('EndBorrowingTime', models.CharField(default='بدون زمان پایان ', max_length=100)),
                ('Descriptions', models.CharField(default='بدون توضیحات', max_length=1000)),
                ('Offered_to_borrow', models.ManyToManyField(to='books.Books')),
                ('Owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='want_to_borrow', to='Users.user')),
            ],
        ),
    ]
