# Generated by Django 3.0.7 on 2020-08-07 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('irc_chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='community',
            field=models.TextField(default='old_messages'),
        ),
    ]
