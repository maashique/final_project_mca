# Generated by Django 4.1.3 on 2023-02-03 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ppApp', '0003_feedback'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='age',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='district',
        ),
    ]