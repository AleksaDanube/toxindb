from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Genomes, Genes, Pfams, PfamsInGenes
from django.core.paginator import Paginator
from django.db.models.functions import Lower
from dna_features_viewer import GraphicFeature, GraphicRecord, CircularGraphicRecord
from io import *
import base64
import random
# Create your views here.
def random_color():
    r = random.randint(0, 0)
    g = random.randint(120, 255)
    b = random.randint(120, 255)
    rand_color = (r/256, g/256, b/256)
    return rand_color
def organisms(request):
    organism_list = []
    organisms = Genomes.objects.order_by(Lower('organism_name').asc())
    organism_list = organisms.values_list("organism_name", flat = True)
    #pfams = Pfams.objects.order_by(Lower('pfam_name').asc())
    #pfams_list = pfams.values_list('pfam_name',flat=True)
    my_dict = {"organism_list":organism_list, "abc": [c for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]}

    return render(request, 'first_app/organisms.html', context = my_dict)
def homepage(request):
    organism_list = []
    organisms = Genomes.objects.order_by(Lower('organism_name').asc())
    organism_list = organisms.values_list("organism_name", flat = True)
    pfams = Pfams.objects.order_by(Lower('pfam_name').asc())
    pfams_list = pfams.values_list('pfam_name',flat=True)
    my_dict = {"organism_list":organism_list, "pfams_list":pfams_list}
    return render(request, 'first_app/toxin-base.html', context = my_dict)
def org_search(request, organism):
    org = Genomes.objects.filter(organism_name__exact = organism)

    org_id_values = org.values("genome_id")

    genes_ids = Genes.objects.filter(genome_id__in = org_id_values).values_list('gene_id', flat = True)

    pfams = PfamsInGenes.objects.filter(gene_id__in = genes_ids)

    genes_list = pfams.values_list('gene_id', flat = True)
    paginator = Paginator(pfams, 25) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    GraphicRecord.labels_spacing = 1
    graphic_pfams_toxins = [GraphicFeature(start = int(pfams[i].pfam_start), end = int(pfams[i].pfam_end), strand = +1, color = random_color(), label = str(pfams[i].pfam_id)) for i,p in enumerate(pfams) if str(pfams[i].toxic_id)=="tox"]
    graphic_pfams_anti = [GraphicFeature(start = int(pfams[i].pfam_start), end = int(pfams[i].pfam_end), strand = +1, color = random_color(), label = str(pfams[i].pfam_id)) for i,p in enumerate(pfams) if str(pfams[i].toxic_id)=="anti-tox"]



    record_tox = GraphicRecord(sequence_length=10000, features=graphic_pfams_toxins)
    record_anti = GraphicRecord(sequence_length=10000, features=graphic_pfams_anti)
    ax1, _ = record_tox.plot(figure_width=12, figure_height = 8)
    #ax1.set_title("toxins")
    buffer = BytesIO()
    ax1.figure.savefig(buffer, format='png')
    ax1.figure.tight_layout()
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    graphic1 = base64.b64encode(image_png)
    graphic1 = graphic1.decode('utf-8')
    ax2, _ = record_anti.plot(figure_width=12, figure_height = 8)
    ax2.figure.tight_layout()
    #ax2.set_title("anti - toxins")
    buffer = BytesIO()
    ax2.figure.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    graphic2 = base64.b64encode(image_png)
    graphic2 = graphic2.decode('utf-8')
    my_dict = {'pfams': pfams, 'organism': organism, 'page_obj': page_obj, 'graph1': graphic1, "graph2": graphic2}
    return render(request, "first_app/organism_search.html", my_dict)
def pfam_search(request, pfam):
    pfam_ids = Pfams.objects.filter(pfam_name__exact = pfam).values_list('pfam_id', flat = True)
    genes_entries = PfamsInGenes.objects.filter(pfam_id__in = pfam_ids)
    gene_ids = genes_entries.values_list('gene_id')
    genome_ids = Genes.objects.filter(gene_id__in = gene_ids).values_list('genome_id', flat = True)
    organisms = Genomes.objects.filter(genome_id__in = genome_ids).values_list('organism_name', flat = True)

    paginator = Paginator(genes_entries, 25) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    my_dict = {"genes_with_pfam": genes_entries, "orgsnism_with_pfams": organisms, 'pfam':pfam, 'page_obj': page_obj}
    return render(request, "first_app/pfam_search.html", my_dict)
def org_list_by_abc(request, first_letter):
    org = Genomes.objects.filter(organism_name__startswith = first_letter.lower())
    org_names = org.values("organism_name")
    my_dict = {'org_list': org_names}
    return render(request, "first_app/org_list_by_abc.html", my_dict)
