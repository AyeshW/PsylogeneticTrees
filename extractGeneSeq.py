import os
import pandas as pd
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

# get df of each species sheet
def read_data(sheet_name, exel_file='protein_tables.xlsx', engine='openpyxl'):
    df = pd.read_excel(exel_file, sheet_name)
    return df

# STEP 3 : extract gene sequence for each protein in protein_set and for each species in common_bacteria_set
def get_homologous_gene_sequences(protein_set, common_bacteria_set):
    genomes = {}
    for p in protein_set:
        new_p = p.replace(" ", "_")
        genomes_of_p = []
        species = []
        for c_b in list(common_bacteria_set):
            species.append(c_b)

            df = read_data(c_b)
            df_p = df.loc[df['Protein name'] == p]
            first_index = df_p.first_valid_index()
            start, stop = df_p.loc[first_index]['Start'], df_p.loc[first_index]['Stop']

            for seq_record in SeqIO.parse(open('fasta/{}.fasta'.format(c_b)), "fasta"):
                c_b_seq = seq_record.seq[start:stop + 1]

            genomes_of_p.append(SeqRecord(c_b_seq, c_b, new_p, ""))
        genomes['p'] = genomes_of_p
        SeqIO.write(genomes_of_p, "out/homologous_gene_sequences/{}.fasta".format(new_p), "fasta")

        with open('out/genomes.txt', 'a') as genomes_file:
            genomes_file.write(p + " - " + str(genomes_of_p))

protein_set = ["porin",
                   "LysR family transcriptional regulator",
                   "helix-turn-helix domain-containing protein",
                   "efflux transporter outer membrane subunit"]

def get_common_bacteria_set(protein_set):
    with open('out/common_bacteria_set.txt', 'r') as f:
        common_bacteria_set = f.read().strip().split("\n")
    return common_bacteria_set


common_bacteria_set = get_common_bacteria_set(protein_set)
get_homologous_gene_sequences(protein_set, common_bacteria_set)