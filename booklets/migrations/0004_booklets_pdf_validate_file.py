# Generated by Django 2.1.7 on 2020-04-22 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booklets', '0003_remove_booklets_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='booklets',
            name='PDF_Validate_File',
            field=models.FileField(blank=True, upload_to='ValPDF/%Y/%m/%d/'),
        ),
    ]
