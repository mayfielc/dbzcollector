# Generated by Django 2.2.3 on 2019-09-14 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('race', models.CharField(max_length=100)),
                ('saga', models.TextField(max_length=250)),
                ('move', models.TextField(max_length=250)),
            ],
        ),
    ]
