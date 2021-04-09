import pandas as pd


# load species sheet to data frame
def read_data(sheet, exel_file='protein_tables.xlsx', engine='openpyxl'):

    df = pd.read_excel(exel_file, sheet)
    return df


def get_common_bacteria_set(protein_set, species):

    print("Calculating the common bacteria set....")
    common_bacteria_set = []

    for specie in species:

        specie_df = read_data(specie)
        specie_protein_set = set(specie_df['Protein name'])
        intersection = set(protein_set).intersection(specie_protein_set)
        if intersection == set(protein_set):
            common_bacteria_set.append(specie)

    print("Calculating common bacteria set completed!", "\n")
    with open("out/common_bacteria_set.txt", "w") as f:
        print("------ Common bacteria set -------")
        for bacteria in common_bacteria_set:
            f.write(bacteria + "\n")
            print(bacteria)
    print("\n")

    return common_bacteria_set
