# Generated by Django 3.2.2 on 2021-08-22 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0003_auto_20210822_1142'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]
