import os
from Bio import AlignIO
from Bio import Phylo
from Bio.Align.Applications import ClustalOmegaCommandline
from Bio.Phylo.TreeConstruction import DistanceCalculator
from Bio.Phylo.TreeConstruction import DistanceTreeConstructor


def build_phylogeny_trees():
    path = "out/homologous_gene_sequences/"
    output_path = "out/aligned_homologous_gene_sequences/"

    for homologous_gene_sequence in os.listdir(path):
        input = path + homologous_gene_sequence
        output = output_path + homologous_gene_sequence
    
        clustal_omega = ClustalOmegaCommandline(infile=input, outfile=output, verbose=True, auto=True)
        os.system(str(clustal_omega))

        multi_seq_align = AlignIO.read(output, 'fasta')

        # Distance Matrix
        calculator = DistanceCalculator('identity')
        dist_mat = calculator.get_distance(multi_seq_align)

        tree_constructor = DistanceTreeConstructor()
        phylo_tree = tree_constructor.upgma(dist_mat)

        Phylo.draw(phylo_tree)

        print('\nPhylogenetic Tree\n', homologous_gene_sequence)
        Phylo.draw_ascii(phylo_tree)
        Phylo.write([phylo_tree], 'out/phylogenetic_trees/{}_tree.nex'.format(homologous_gene_sequence), 'nexus')
