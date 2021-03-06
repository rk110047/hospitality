# Generated by Django 3.1.4 on 2021-01-25 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0004_auto_20210114_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fooditem',
            name='item_description',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='fooditem',
            name='item_image',
            field=models.ImageField(blank=True, null=True, upload_to='food item images/'),
        ),
    ]
