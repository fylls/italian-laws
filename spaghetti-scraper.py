import os
import sys

# main library used to extract text from PDFs (used by OpenAI)
from pdfminer.high_level import extract_text


def get_text(file_name):

    # status
    print(f"mining {file_name} ...")

    # check if file exists
    if not os.path.exists(f"./PDFs/{file_name}"): print("file doesn't exits"); return

    # mine it if exists
    text = extract_text(f"./PDFs/{file_name}")
    
    # name output directory
    name = file_name.rsplit(".", 1)[0]

    # output dir
    output_dir= f"./TXTs/{name}"
 
    # check if folder exists, create it if it doesn't
    if not os.path.exists(output_dir): os.makedirs(output_dir)

    # save extracted text
    with open(f"{output_dir}/mined.txt", "w") as f: f.write(text)

    # status
    print(f"text succesfully extracted")
    print(f"{'_'*120}\n")



def main():
    
    # status
    print("Enter 'stop' to quit")

    # contol flow
    while True:

        # ask user the name of the file
        file_name = input("what file do you want to mine? ")

        # user asked to mine all files
        if file_name == "all files":

            # get all the files in directory
            files = os.listdir('./PDFs')

            # mine them one by one
            for file in files: get_text(file)
    
        # get out of the loop if asked
        elif file_name == 'stop': sys.exit()

        # just mine the specified file
        else: get_text(file_name)



main()