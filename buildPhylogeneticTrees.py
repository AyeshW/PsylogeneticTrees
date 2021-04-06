import os
from Bio import AlignIO
from Bio import Phylo
from Bio.Align.Applications import ClustalOmegaCommandline
from Bio.Phylo.TreeConstruction import DistanceCalculator
from Bio.Phylo.TreeConstruction import DistanceTreeConstructor

# STEP 4 : build phylogenetic trees
def build_phylogeny_trees():
    path = "out/homologous_gene_sequences/"
    out_path = "out/aligned_homologous_gene_sequences/"

    for homologous_gene_sequence in os.listdir(path):
        in_file = path + homologous_gene_sequence
        out_file = out_path + homologous_gene_sequence
    
        clustalomega_cline = ClustalOmegaCommandline(infile=in_file, outfile=out_file, verbose=True, auto=True)
        os.system(str(clustalomega_cline))

        msa = AlignIO.read(out_file, 'fasta')

        # Calculate the distance matrix
        calculator = DistanceCalculator('identity')
        dm = calculator.get_distance(msa)

        # Print the distance Matrix
        print('\nDistance Matrix\n===================')
        print(dm)

        # Construct the phylogenetic tree using UPGMA algorithm
        constructor = DistanceTreeConstructor()
        tree = constructor.upgma(dm)

        # Draw the phylogenetic tree
        Phylo.draw(tree)

        # Print the phylogenetic tree in the terminal
        print('\nPhylogenetic Tree\n', homologous_gene_sequence)
        Phylo.draw_ascii(tree)
        Phylo.write([tree], 'out/trees/{}_tree.nex'.format(homologous_gene_sequence), 'nexus')

build_phylogeny_trees()