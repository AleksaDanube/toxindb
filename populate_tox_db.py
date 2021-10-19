import os
import pandas
from decimal import Decimal
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'toxins_project.settings')

import django
# Import settings
django.setup()
from first_app.models import Genomes, Genes, Pfams, PfamsInGenes
tox_data_csv = "toxinome_tox_final_mini.csv"
anti_tox_data_csv = "toxinome_anti_final_mini.csv"


tox_df = pandas.read_csv(tox_data_csv)
tox_df = tox_df.fillna('na')
tox_df = tox_df.applymap(str)
tox_df.to_csv('new_db.csv')
antitox_df = pandas.read_csv(anti_tox_data_csv)
antitox_df = antitox_df.fillna('na')
antitox_df = antitox_df.applymap(str)

print('start population')
for index, row in tox_df.iterrows():
    genome_id_from_df = row['genome']
    organism_id_from_df = row['organism']
    scaffold_from_df = row['seqID']
    gene_id_from_df = row['proteinID']
    gene_len_from_df = int(float(row['gene_length']))
    gene_start_from_df = int(float(row['start']))
    gene_end_from_df = int(float(row['end']))
    gene_strand_orientation_from_df = row['strand']
    product_name_from_df = row['product_name']
    protein_tox = "tox"
    pfam_id_from_df = row['pfamID']
    pfam_name_from_df = row['pfam_name']
    pfam_len_from_df = int(float(row['pfam_length']))
    toxicity_from_df = row['pfam_toxity']
    pfam_start_from_df = int(float(row['pfam_start']))
    pfam_end_from_df = int(float(row['pfam_end']))
    # bit_score_from_df = float(row['pfam_bit_score'])
    # e_value_from_df = str("{:.2E}".format(Decimal(row['pfam_e_val'])))
    gnms = Genomes.objects.get_or_create(genome_id = genome_id_from_df,
                                         organism_name = organism_id_from_df)[0]
    gnms.save()
    gns = Genes.objects.get_or_create(gene_id = gene_id_from_df,
                                      scaffold = scaffold_from_df,
                                      genome_id = gnms,
                                      gene_len = gene_len_from_df,
                                      start = gene_start_from_df,
                                      end = gene_end_from_df,
                                      strand = gene_strand_orientation_from_df,
                                      product_name = product_name_from_df,
                                      protein_toxicity = protein_tox )[0]
    gns.save()
    pfms = Pfams.objects.get_or_create(pfam_id = pfam_id_from_df,
                                       pfam_name = pfam_name_from_df,
                                       pfam_len = pfam_len_from_df,
                                       toxic_id = toxicity_from_df)[0]
    pfms.save()
    pfmsngns = PfamsInGenes.objects.get_or_create(gene_id = gns,
                                                  organism_name = organism_id_from_df,
                                                  pfam_id = pfms,
                                                  toxic_id = toxicity_from_df,
                                                  pfam_start = pfam_start_from_df,
                                                  pfam_end = pfam_end_from_df)[0]
                                                  # bit_score = bit_score_from_df,
                                                  # e_val = e_value_from_df)[0]
    pfmsngns.save()
print("done with toxins")
#
for index, row in antitox_df.iterrows():
    genome_id_from_df = row['genome']
    organism_id_from_df = row['organism']
    scaffold_from_df = row['seqID']
    gene_id_from_df = row['proteinID']
    gene_len_from_df = int(float(row['gene_length']))
    gene_start_from_df = int(float(row['start']))
    gene_end_from_df = int(float(row['end']))
    gene_strand_orientation_from_df = row['strand']
    product_name_from_df = row['product_name']
    protein_tox = "anti-tox"
    pfam_id_from_df = row['pfamID']
    pfam_name_from_df = row['pfam_name']
    pfam_len_from_df = int(float(row['pfam_length']))
    toxicity_from_df = row['pfam_toxity']
    pfam_start_from_df = int(float(row['pfam_start']))
    pfam_end_from_df = int(float(row['pfam_end']))
    # bit_score_from_df = float(row['pfam_bit_score'])
    # e_value_from_df = str("{:.2E}".format(Decimal(row['pfam_e_val'])))
    gnms = Genomes.objects.get_or_create(genome_id = genome_id_from_df,
                                         organism_name = organism_id_from_df)[0]
    gnms.save()
    gns = Genes.objects.get_or_create(gene_id = gene_id_from_df,
                                      scaffold = scaffold_from_df,
                                      genome_id = gnms,
                                      gene_len = gene_len_from_df,
                                      start = gene_start_from_df,
                                      end = gene_end_from_df,
                                      strand = gene_strand_orientation_from_df,
                                      product_name = product_name_from_df,
                                      protein_toxicity = protein_tox )[0]
    gns.save()
    pfms = Pfams.objects.get_or_create(pfam_id = pfam_id_from_df,
                                       pfam_name = pfam_name_from_df,
                                       pfam_len = pfam_len_from_df,
                                       toxic_id = toxicity_from_df)[0]
    pfms.save()
    pfmsngns = PfamsInGenes.objects.get_or_create(gene_id = gns,
                                                  organism_name = organism_id_from_df,
                                                  pfam_id = pfms,
                                                  toxic_id = toxicity_from_df,
                                                  pfam_start = pfam_start_from_df,
                                                  pfam_end = pfam_end_from_df)[0]
                                                  # bit_score = bit_score_from_df,
                                                  # e_val = e_value_from_df)[0]
    pfmsngns.save()
print("done with anti toxins")
