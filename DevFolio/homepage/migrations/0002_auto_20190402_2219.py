# Generated by Django 2.1.7 on 2019-04-03 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='snippet',
            old_name='body',
            new_name='content',
        ),
        migrations.AddField(
            model_name='snippet',
            name='mail',
            field=models.CharField(default='Enter your Email', max_length=75),
        ),
        migrations.AddField(
            model_name='snippet',
            name='subject',
            field=models.CharField(default='Enter a Subject', max_length=100),
        ),
        migrations.AlterField(
            model_name='snippet',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
