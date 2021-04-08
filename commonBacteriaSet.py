import os
import pandas as pd

# get df of each species sheet
def read_data(sheet_name, exel_file='protein_tables.xlsx', engine='openpyxl'):
    df = pd.read_excel(exel_file, sheet_name)
    return df

# get common bacteria set
def get_common_bacteria_set(protein_set, species):
    print("Calculating common bacteria set")
    common_bacteria_set = []
    for _ in species:
        specie_df = read_data(_)
        proteins_set_in_specie = set(specie_df['Protein name'])
        set_intersection = set(protein_set).intersection(proteins_set_in_specie)
        if set_intersection == set(protein_set):
            common_bacteria_set.append(_)
    print("Calculating common bacteria set completed", "\n")
    with open("out/common_bacteria_set.txt", "w") as f:
        print("------ Common bacteria set -------")
        for i in common_bacteria_set:
            f.write(i + "\n")
            print(i)
    print("\n")
    return common_bacteria_set