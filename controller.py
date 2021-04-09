import pandas as pd

from buildPhylogeneticTrees import build_phylogeny_trees
from commonBacteriaSet import get_common_bacteria_set
from extractGeneSeq import get_homologous_gene_sequences
from robinsonFouldsDistance import calc_robinson_foulds_distance

if __name__ == "__main__":

    protein_set = ["porin",
                   "LysR family transcriptional regulator",
                   "helix-turn-helix domain-containing protein",
                   "efflux transporter outer membrane subunit"]

    excel_file = pd.ExcelFile('protein_tables.xlsx')
    species = excel_file.sheet_names

    # step 1 - Get common bacteria set
    common_bacteria_set = get_common_bacteria_set(protein_set, species)

    # step 2 - Download the gene sequence of species in common_bacteria_set
    print("You need to download the gene sequence of species in common_bacteria_set")
    print("---- We have downloded for you. You can find those in fasta folder ----")

    # step 3 - Extract gene sequence for each protein in protein_set and for each species in common_bacteria_set
    get_homologous_gene_sequences(protein_set, common_bacteria_set)

    # step 4 - Build phylogenetic trees
    build_phylogeny_trees()

    # step 5 - Calculate the distance (difference) between each pair of trees
    calc_robinson_foulds_distance()

