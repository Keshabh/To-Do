# Generated by Django 3.2.5 on 2021-12-24 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0004_progress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='progress',
            name='date',
            field=models.CharField(max_length=200),
        ),
    ]
