# Generated by Django 2.1.7 on 2020-05-11 17:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0013_wishlist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proposed_book',
            name='Proposed_book',
        ),
        migrations.AddField(
            model_name='proposed_book',
            name='Proposed_book',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='proposedBook', to='books.Books'),
        ),
    ]
