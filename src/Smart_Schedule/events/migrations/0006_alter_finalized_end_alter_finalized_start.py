# Generated by Django 4.1.2 on 2022-11-11 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_finalized'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finalized',
            name='end',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='finalized',
            name='start',
            field=models.TimeField(),
        ),
    ]
