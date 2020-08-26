# Generated by Django 3.0.7 on 2020-08-10 23:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InstallationInstruction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='InstallationStep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveSmallIntegerField()),
                ('text', models.TextField()),
                ('installation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='install.InstallationInstruction')),
            ],
            options={
                'ordering': ('order',),
            },
        ),
        migrations.CreateModel(
            name='Software',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('software', models.CharField(max_length=250, unique=True)),
                ('operating_system', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Screenshot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveSmallIntegerField()),
                ('image', models.ImageField(upload_to='')),
                ('installation_step', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='screenshots', to='install.InstallationStep')),
            ],
            options={
                'ordering': ('order',),
            },
        ),
        migrations.AddField(
            model_name='installationinstruction',
            name='software',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='install.Software'),
        ),
    ]
