# Generated by Django 3.2 on 2021-07-14 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20210714_1529'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description2',
            field=models.TextField(blank=True),
        ),
    ]
