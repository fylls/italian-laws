import re
import csv
import sys
import os


def parse_text(dir_name):

    # status
    print(f"parsing {dir_name} ...")

    # final parsed text
    text = ""

    # define input path
    file_path = f"./TXTs/{dir_name}/mined.txt"

    # check if file exists
    if not os.path.exists(file_path): print("file doesn't exits"); return

    # open file in reading mode
    with open(file_path, "r") as file:

        # read it line by line
        for line in file:

            # delete an entire line if the first two letters are uppercase
            if re.match("^[A-Z]{2,}", line): line = ""
            
            # delete line if it has a weird character
            if len(line) > 2:
                if line[0] == "§": line = ""

            # remove ucnnecessary spaces
            line = re.sub(r'  +', ' ', line)

            # add paesed line to text
            text = text + line + ""


    # remove multiple whitespacy characters
    text = re.sub(r'\s\s+', ' ', text)
    text = re.sub(r'__+', ' ', text)
    text = re.sub(r'--+', ' ', text)
    text = text.replace("", "")

    # ordered text
    text = "\nArt.".join(text.split("Art."))

    # define output path
    output_path = f"./TXTs/{dir_name}"

    # output document
    with open(f"{output_path}/parsed.txt", "w") as f: f.write(text)

    # parse list
    list = text.split("Art.")

    # Save the dictionary as a TSV file
    tsv = ""
    for article in list: tsv += f"{dir_name}\tArt.{article}"
    with open(f"{output_path}/index.tsv", "w") as f: f.write(tsv)


def main():
    
    # status
    print("Enter 'stop' to quit")

    # contol flow
    while True:

        # ask user the name of the directory
        dir_name = input("what directories do you want to parse? ")

        # user asked to mine all files
        if dir_name == "all dirs":

            # get all the files in directory
            dirs = os.listdir("./TXTs")

            # mine them one by one
            for d in dirs: parse_text(d)
    
        # get out of the loop if asked
        elif dir_name == 'stop': sys.exit()

        # just mine the specified directory
        else: parse_text(dir_name)


main()

# to improve on
# - culturali
# - turismo
# - norme di mareria ambientale
# regolamento di esecuzione e di attuazione del nuovo codice della strada
# - elimina gli abrogati