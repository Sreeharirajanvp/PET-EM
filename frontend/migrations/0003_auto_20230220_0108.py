# Generated by Django 3.2.10 on 2023-02-19 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0002_auto_20230216_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='savelogindb',
            name='Confirm',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='savelogindb',
            name='Password',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
