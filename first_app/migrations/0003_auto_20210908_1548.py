# Generated by Django 3.2.5 on 2021-09-08 12:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0002_alter_pfamsingenes_e_val'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pfamsingenes',
            name='gene_id',
        ),
        migrations.RemoveField(
            model_name='pfamsingenes',
            name='pfam_id',
        ),
        migrations.DeleteModel(
            name='Genes',
        ),
        migrations.DeleteModel(
            name='Genomes',
        ),
        migrations.DeleteModel(
            name='Pfams',
        ),
        migrations.DeleteModel(
            name='PfamsInGenes',
        ),
    ]