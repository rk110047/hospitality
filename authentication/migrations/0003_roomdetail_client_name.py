# Generated by Django 3.1.4 on 2021-01-23 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_roomdetail'),
    ]

    operations = [
        migrations.AddField(
            model_name='roomdetail',
            name='client_name',
            field=models.CharField(default=1, max_length=120),
            preserve_default=False,
        ),
    ]
