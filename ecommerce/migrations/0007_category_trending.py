# Generated by Django 3.2.2 on 2021-08-26 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0006_alter_subcategory_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='trending',
            field=models.BooleanField(default=False),
        ),
    ]
