import json
import os
import dendropy


# calculate the distance (difference) between each pair of trees
def calc_robinson_foulds_distance():
    print("Robinson Foulds Distances between Trees")
    print("---------------------------------------")
    robinson_foulds_distances = {}

    for tree_i in os.listdir('out/phylogenetic_trees'):
        robinson_foulds_distances[tree_i] = {}

        for tree_j in os.listdir('out/phylogenetic_trees'):
            if tree_i >= tree_j:
                continue

            else:
                taxon_nmspce = dendropy.TaxonNamespace()
                treeA = dendropy.Tree.get_from_path(
                    'out/phylogenetic_trees/{}'.format(tree_i),
                    'nexus',
                    taxon_namespace=taxon_nmspce, )

                treeB = dendropy.Tree.get_from_path(
                    'out/phylogenetic_trees/{}'.format(tree_j),
                    "nexus",
                    taxon_namespace=taxon_nmspce)

                treeA.encode_bipartitions()
                treeB.encode_bipartitions()
                distance = round(dendropy.calculate.treecompare.
                                 weighted_robinson_foulds_distance(treeA, treeB), 4)
                robinson_foulds_distances[tree_i][tree_j] = distance
                print(tree_i, "AND", tree_j, distance, "\n")

    with open('out/robinson_foulds_distances_between_trees.json', 'w') as file:
        json.dump(robinson_foulds_distances, file)
