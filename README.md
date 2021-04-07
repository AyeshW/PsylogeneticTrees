# PsylogeneticTrees
## Instructions
1. Clone the repository.
2. Open a command line/ terminal.
3. Give following commands.

```
sudo apt install clustalo
sudo apt install python3-pip
pip3 install -r requirements.txt
```

## Steps
1. Get common bacteria set
```
python3 commonBacteriaSet.py
```
2. Download the gene sequence of species in common_bacteria_set
3. Extract gene sequence for each protein in protein_set and for each species in common_bacteria_set
```
python3 extractGeneSeq.py
```
4.  Build phylogenetic trees
```
python3 buildPhylogeneticTrees.py
```