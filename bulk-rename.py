import os
import csv
import re

# Use an absolute path to the directory where your files are located
DIR = os.getcwd()
data = []
data_len = len(data)

exclude_filenames = ["bulk-rename.py", "data.csv"]  # Add the filenames you want to skip here

# Define a function to extract the numeric part of a filename using regex
def extract_numeric_part(filename):
    match = re.search(r'(\d+)', filename)
    return int(match.group()) if match else float('inf')

def main():
    with open('data.csv', 'r', encoding='ISO-8859-1') as csvfile:
        csvreader = csv.reader(csvfile)
        
        for row in csvreader:
            name = row
            name = str(name)
            name = name.replace(",", "")
            data.append(name)
    
    # Sort the filenames numerically
    sorted_filenames = sorted(os.listdir(DIR), key=extract_numeric_part)
    
    for filename in sorted_filenames:
        if filename not in exclude_filenames:
            f = os.path.join(DIR, filename)
            if os.path.isfile(f):
                newname = str(data.pop(0)) + "_Certificate_DCISM_Community_Day_23-24_Prelim"+".png" #rename this for the 
                newname = newname.replace("'","")
                newname = newname.replace("[","")
                newname = newname.replace("]","")
                print(newname)
                os.rename(f, os.path.join(DIR, newname))

if __name__ == "__main__":
    main()
