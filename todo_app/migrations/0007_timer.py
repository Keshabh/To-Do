# Generated by Django 3.2.5 on 2021-12-27 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0006_auto_20211224_2231'),
    ]

    operations = [
        migrations.CreateModel(
            name='Timer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.IntegerField(default=120)),
            ],
        ),
    ]
