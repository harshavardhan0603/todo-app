# Generated by Django 4.1.4 on 2022-12-27 08:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_tasks_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tasks',
            name='user',
        ),
    ]
