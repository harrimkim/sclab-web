# Generated by Django 2.0.6 on 2018-06-27 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0010_merge_20180628_0016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='date',
            field=models.CharField(max_length=200),
        ),
    ]
