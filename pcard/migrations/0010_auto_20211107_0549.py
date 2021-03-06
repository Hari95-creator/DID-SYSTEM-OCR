# Generated by Django 3.2.7 on 2021-11-07 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pcard', '0009_auto_20211107_0455'),
    ]

    operations = [
        migrations.CreateModel(
            name='aadharapi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=100, unique=True)),
                ('aadharno', models.CharField(max_length=100)),
                ('pname', models.CharField(max_length=100)),
                ('fname', models.CharField(max_length=100)),
                ('dob', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='drvingapi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=100, unique=True)),
                ('licenceno', models.CharField(max_length=100)),
                ('licencename', models.CharField(max_length=100)),
                ('fathername', models.CharField(max_length=100)),
                ('dob', models.CharField(max_length=100)),
                ('issuedate', models.CharField(max_length=100)),
                ('validate', models.CharField(max_length=100)),
                ('authtodr', models.CharField(max_length=100)),
                ('authtodrive', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='voterapi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voterfname', models.CharField(max_length=100)),
                ('votername', models.CharField(max_length=100)),
                ('voterid', models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameModel(
            old_name='api',
            new_name='panapi',
        ),
        migrations.RemoveField(
            model_name='aadhardb',
            name='aadharno',
        ),
        migrations.RemoveField(
            model_name='voteriddata',
            name='voterid',
        ),
    ]
