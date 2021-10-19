from django.db import models

# Create your models here.
class Genomes(models.Model):
    genome_id = models.CharField(max_length = 264, unique = True, primary_key=True)
    organism_name = models.CharField(max_length = 264)
    #scaffold = models.CharField(max_length = 264, unique = True, primary_key=True)
    def __str__(self):
        return self.genome_id
class Genes(models.Model):
    genome_id = models.ForeignKey(Genomes, on_delete = models.CASCADE )
    gene_id = models.CharField(max_length = 264, unique = True, primary_key=True)
    scaffold = models.CharField(max_length = 264)
    gene_len = models.IntegerField()
    start = models.IntegerField()
    end = models.IntegerField()
    strand = models.CharField(max_length = 1)
    product_name = models.CharField(max_length = 264)
    protein_toxicity = models.CharField(max_length = 264)
    def __str__(self):
        return self.gene_id
class Pfams(models.Model):
    pfam_id = models.CharField(max_length = 264, unique = True, primary_key=True)
    pfam_name = models.CharField(max_length = 264)
    pfam_len = models.IntegerField()
    toxic_id = models.CharField(max_length = 264)
    def __str__(self):
        return self.pfam_name
class PfamsInGenes(models.Model):
    id = models.BigAutoField(primary_key=True)
    gene_id = models.ForeignKey(Genes, on_delete = models.CASCADE)
    organism_name = models.CharField(max_length = 264)
    pfam_id = models.ForeignKey(Pfams, on_delete = models.CASCADE)
    toxic_id = models.CharField(max_length = 264)
    pfam_start = models.IntegerField()
    pfam_end = models.IntegerField()
    # bit_score = models.FloatField()
    # e_val = models.CharField(max_length = 264)
    def __str__(self):
       return str(self.id)
