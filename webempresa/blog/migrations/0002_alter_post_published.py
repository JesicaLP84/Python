# Generated by Django 4.0.1 on 2023-02-22 10:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 22, 10, 26, 37, 442682, tzinfo=utc), verbose_name='Fecha de publicación'),
        ),
    ]