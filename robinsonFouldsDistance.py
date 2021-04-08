import json
import os
import dendropy


def calc_robinson_foulds_distance():

    print("Robinson Foulds Distances between Trees\n")
    robinson_foulds_distances = {}

    for tree_i in os.listdir('out/phylogenetic_trees'):
        robinson_foulds_distances[tree_i] = {}
        print(tree_i, "\n")

        for tree_j in os.listdir('out/phylogenetic_trees'):
            if tree_i >= tree_j:
                continue

            else:
                taxon_nmspce = dendropy.TaxonNamespace()
                treeA = dendropy.Tree.get_from_path(
                    'out/phylogenetic_trees/{}'.format(tree_i),
                    'nexus',
                    taxon_namespace=taxon_nmspce,)

                treeB = dendropy.Tree.get_from_path(
                    'out/phylogenetic_trees/{}'.format(tree_j),
                    "nexus",
                    taxon_namespace=taxon_nmspce)

                treeA.encode_bipartitions()
                treeB.encode_bipartitions()
                robinson_foulds_distances[tree_i][tree_j] = round(dendropy.calculate.treecompare.
                                                       weighted_robinson_foulds_distance(treeA, treeB), 4)
        print("\n")
    with open('out/robinson_foulds_distances_between_trees.json', 'w') as file:
        json.dump(robinson_foulds_distances, file)


calc_robinson_foulds_distance()

