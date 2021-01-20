# Generated by Django 3.0 on 2021-01-20 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', models.CharField(max_length=1000)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('author', models.CharField(max_length=40)),
            ],
        ),
    ]
