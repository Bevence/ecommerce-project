# Generated by Django 3.2.2 on 2021-08-26 13:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0010_subcategory_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subcategory',
            name='count',
        ),
    ]