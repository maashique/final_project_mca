# Generated by Django 4.1.3 on 2023-05-18 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ppApp', '0020_remove_registration_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='address',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='registration',
            name='prof',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
