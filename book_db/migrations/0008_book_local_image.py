# Generated by Django 2.2.2 on 2019-07-03 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_db', '0007_book_volume'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='local_image',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to=''),
        ),
    ]
