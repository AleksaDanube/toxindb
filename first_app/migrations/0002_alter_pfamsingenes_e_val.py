# Generated by Django 3.2.5 on 2021-09-08 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pfamsingenes',
            name='e_val',
            field=models.CharField(max_length=264),
        ),
    ]
