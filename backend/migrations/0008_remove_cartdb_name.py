# Generated by Django 3.2.10 on 2023-02-20 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_auto_20230220_0108'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartdb',
            name='Name',
        ),
    ]
