# Generated by Django 3.0.7 on 2020-09-10 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Term',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term', models.TextField()),
                ('slug', models.CharField(blank=True, max_length=200)),
                ('explication', models.TextField()),
                ('readings', models.ManyToManyField(to='library.Reading')),
                ('tutorials', models.ManyToManyField(to='library.Tutorial')),
            ],
            options={
                'ordering': ['term'],
            },
        ),
    ]
