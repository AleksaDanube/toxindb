from django.contrib import admin
from first_app.models import Genomes, Genes, Pfams, PfamsInGenes
# Register your models here.
admin.site.register(Genomes)
admin.site.register(Genes)
admin.site.register(Pfams)
admin.site.register(PfamsInGenes)
