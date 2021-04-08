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
    common_bacteria_set = get_common_bacteria_set(protein_set, species)

    get_homologous_gene_sequences(protein_set, common_bacteria_set)

    build_phylogeny_trees()

    calc_robinson_foulds_distance()

