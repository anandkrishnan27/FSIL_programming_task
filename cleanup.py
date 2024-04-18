import os

def main():
    folderpath = "/Users/anandkrishnan/Desktop/FSIL project/sec-edgar-filings/financial_statements"

    files = os.listdir(folderpath)

    for file in files:
        filepath = os.path.join(folderpath, file)
        os.remove(filepath)