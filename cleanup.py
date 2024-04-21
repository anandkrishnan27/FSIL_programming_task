"""
cleanup.py contains functions that delete all downloaded files from the local directory
"""
import os

"""
Function main(): removes all files containing written item 7a. in the "financial_statements" local folder 
"""
def main():
    folderpath = "/Users/anandkrishnan/Desktop/FSIL project/sec-edgar-filings/financial_statements"
    files = os.listdir(folderpath)

    for file in files:
        filepath = os.path.join(folderpath, file)
        os.remove(filepath)
