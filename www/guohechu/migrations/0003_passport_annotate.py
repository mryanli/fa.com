# Generated by Django 2.0.4 on 2018-08-22 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guohechu', '0002_auto_20180821_2331'),
    ]

    operations = [
        migrations.AddField(
            model_name='passport',
            name='annotate',
            field=models.TextField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
