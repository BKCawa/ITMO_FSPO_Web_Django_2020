# Generated by Django 3.0.7 on 2020-11-02 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fur_shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='farm',
            managers=[
            ],
        ),
        migrations.RenameField(
            model_name='purchase',
            old_name='coat',
            new_name='fur',
        ),
    ]