# Generated by Django 3.0.7 on 2020-11-02 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fur_shop', '0002_auto_20201102_1423'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='user_id',
            field=models.IntegerField(default=0),
        ),
    ]
