import os

# get the names of all the directories
dirs = os.listdir('./TXTs')

# full index
conplete_index = ""

# loop trough every directory
for d in dirs:
     
    # find the TSV file for each legal text
    with open(f"./TXTs/{d}/index.tsv", "r") as file:

        # turn TextIOWrapper to strinf
        index = file.read()

        # add all the indexes together
        conplete_index += index

# save them in the root directory
with open("./index.tsv", "w") as f: f.write(conplete_index)
