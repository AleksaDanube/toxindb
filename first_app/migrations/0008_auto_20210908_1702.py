# Generated by Django 3.2.5 on 2021-09-08 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0007_auto_20210908_1657'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pfamsingenes',
            name='numb',
        ),
        migrations.AddField(
            model_name='pfamsingenes',
            name='id',
            field=models.BigAutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]