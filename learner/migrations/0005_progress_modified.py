# Generated by Django 3.0.7 on 2020-10-23 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learner', '0004_progress'),
    ]

    operations = [
        migrations.AddField(
            model_name='progress',
            name='modified',
            field=models.DateField(auto_now=True),
        ),
    ]
