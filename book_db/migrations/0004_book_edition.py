# Generated by Django 2.2.2 on 2019-07-01 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_db', '0003_auto_20190701_1324'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='edition',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
