# Generated by Django 3.0.8 on 2020-08-04 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('earlydating', '0002_auto_20200804_0024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='preference',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other'), ('Both', 'Both')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='sex',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='uservote',
            name='vote',
            field=models.BooleanField(default=''),
        ),
    ]
