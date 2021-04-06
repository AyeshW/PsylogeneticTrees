import os
import pandas as pd

# get df of each species sheet
def read_data(sheet_name, exel_file='protein_tables.xlsx', engine='openpyxl'):
    df = pd.read_excel(exel_file, sheet_name)
    return df

# STEP 1 : get common bacteria set
def get_common_bacteria_set(protein_set, species):
    common_bacteria_set = []
    for _ in species:
        specie_df = read_data(_)
        proteins_set_in_specie = set(specie_df['Protein name'])
        set_intersection = set(protein_set).intersection(proteins_set_in_specie)
        if set_intersection == set(protein_set):
            common_bacteria_set.append(_)
    with open("out/common_bacteria_set.txt", "w") as f:
        for i in common_bacteria_set:
            f.write(i + "\n")
            print(i)
    print("\n")
    return common_bacteria_set


protein_set = ["porin",
                   "LysR family transcriptional regulator",
                   "helix-turn-helix domain-containing protein",
                   "efflux transporter outer membrane subunit"]

excel_file = pd.ExcelFile('protein_tables.xlsx')
species = excel_file.sheet_names
common_bacteria_set = get_common_bacteria_set(protein_set, species)