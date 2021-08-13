# Generated by Django 3.2.5 on 2021-08-10 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='passwordreset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.IntegerField()),
                ('token', models.CharField(max_length=250)),
                ('isvalid', models.IntegerField()),
                ('validtill', models.DateTimeField()),
            ],
            options={
                'db_table': 'PasswordReset',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Proposalmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('fname', models.CharField(max_length=250)),
                ('lname', models.CharField(max_length=250)),
                ('phone', models.IntegerField()),
                ('email', models.CharField(max_length=250)),
                ('userType', models.CharField(max_length=250)),
                ('status', models.CharField(max_length=255)),
                ('ptitle', models.CharField(max_length=250)),
                ('pdesc', models.CharField(max_length=250)),
                ('pwebsite', models.CharField(max_length=250)),
                ('comment', models.CharField(max_length=250)),
                ('reference', models.CharField(max_length=250)),
                ('document', models.CharField(max_length=250)),
            ],
            options={
                'db_table': 'proposals',
            },
        ),
    ]
