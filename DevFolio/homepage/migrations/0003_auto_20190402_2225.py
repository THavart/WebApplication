# Generated by Django 2.1.7 on 2019-04-03 02:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_auto_20190402_2219'),
    ]

    operations = [
        migrations.RenameField(
            model_name='snippet',
            old_name='mail',
            new_name='email',
        ),
    ]
