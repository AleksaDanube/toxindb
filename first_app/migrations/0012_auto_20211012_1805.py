# Generated by Django 3.2.5 on 2021-10-12 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0011_genes_genomes_pfams_pfamsingenes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pfamsingenes',
            name='bit_score',
        ),
        migrations.RemoveField(
            model_name='pfamsingenes',
            name='e_val',
        ),
    ]
