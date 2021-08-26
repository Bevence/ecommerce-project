# Generated by Django 3.2.2 on 2021-08-22 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='items',
            options={'verbose_name_plural': 'Items'},
        ),
        migrations.AddField(
            model_name='category',
            name='count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='items',
            name='count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='items',
            name='image',
            field=models.ImageField(upload_to='ecommerce/media/items/'),
        ),
    ]
