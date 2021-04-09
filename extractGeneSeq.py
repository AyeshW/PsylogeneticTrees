import pandas as pd
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord


# load species sheet to fata frame
def read_data(sheet, exel_file='protein_tables.xlsx', engine='openpyxl'):

    df = pd.read_excel(exel_file, sheet)
    return df


# extract gene sequence
def get_homologous_gene_sequences(protein_set, common_bacteria_set):

    genes = {}
    for protein in protein_set:
        new_protein = protein.replace(" ", "_")
        protein_genes = []
        species = []

        for bacteria in list(common_bacteria_set):
            species.append(bacteria)
            df = read_data(bacteria)
            df_protein = df.loc[df['Protein name'] == protein]
            first_index = df_protein.first_valid_index()
            # start, stop = df_protein.loc[first_index]['Start'], df_protein.loc[first_index]['Stop']
            start = df_protein.loc[first_index]['Start']
            stop = df_protein.loc[first_index]['Stop']

            for record in SeqIO.parse(open('fasta/{}.fasta'.format(bacteria)), "fasta"):
                bacteria_seq = record.seq[start:stop + 1]

            protein_genes.append(SeqRecord(bacteria_seq, bacteria, new_protein, ""))

        genes['protein'] = protein_genes
        SeqIO.write(protein_genes, "out/homologous_gene_sequences/{}.fasta".format(new_protein), "fasta")

        with open('out/genes.txt', 'a') as genes_file:
            genes_file.write(protein + " - " + str(protein_genes))
