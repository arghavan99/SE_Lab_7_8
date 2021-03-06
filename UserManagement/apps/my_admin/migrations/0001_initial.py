# Generated by Django 4.0 on 2021-12-16 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('name', models.CharField(max_length=100)),
                ('national_id', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('admin', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
