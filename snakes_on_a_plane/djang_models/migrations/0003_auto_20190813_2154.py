# Generated by Django 2.2.4 on 2019-08-13 21:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djang_models', '0002_auto_20190813_2152'),
    ]

    operations = [
        migrations.RenameField(
            model_name='seats',
            old_name='name',
            new_name='seatnumber',
        ),
    ]