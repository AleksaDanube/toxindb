# Generated by Django 3.2.5 on 2021-09-08 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0006_alter_pfams_toxic_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pfamsingenes',
            name='id',
        ),
        migrations.AddField(
            model_name='pfamsingenes',
            name='numb',
            field=models.IntegerField(default=1, primary_key=True, serialize=False, unique=True),
            preserve_default=False,
        ),
    ]
