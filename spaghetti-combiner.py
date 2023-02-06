import os

# full index
complete_index = ""

# get the names of all the directories
directories = os.listdir('./TXTs')

# loop trough every directory
for directory in directories:
     
    # find the ultimate.txt file for each directory
    with open(f"./TXTs/{directory}/ultimate.txt", "r") as file:

        # convert TextIOWrapper to string
        text = file.read() + "\n"

        # split text into a list 
        list = text.split("Art.")

        # add list to TSV file
        for article in list: 

            # avoid adding it if the line is empty-ish
            if len(article) > 2:

                # add article to index
                complete_index += f"{directory}\tArt.{article}"

# save them in the root directory
with open("./index.tsv", "w") as f: f.write(complete_index)
