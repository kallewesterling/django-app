# Generated by Django 3.0.7 on 2020-07-09 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='is_homepage',
        ),
        migrations.AddField(
            model_name='page',
            name='template',
            field=models.CharField(default='website/page.html', max_length=100),
        ),
    ]
