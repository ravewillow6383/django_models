# Generated by Django 2.2.4 on 2019-08-13 22:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djang_models', '0003_auto_20190813_2244'),
    ]

    operations = [
        migrations.RenameField(
            model_name='passenger',
            old_name='seatnumber',
            new_name='name',
        ),
    ]
