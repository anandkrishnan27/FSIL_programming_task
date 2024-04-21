"""
parse.py contains functions that take the downloaded 10-K filings and extract item 7a. (risk profile)
to a specified location on the desktop locally
"""
from bs4 import BeautifulSoup
import downloader
import os

"""
Function find_nth(): given an input string, this function finds the n'th occurence of a given substring
in the original string and returns its index
@ param input: initial string
@ param substring: string that appears at least once in the original string
@ param n: which occurence of the substring we want to capture
@ return start: start index for the substring within the original string
"""
def find_nth(input, substring, n):
    start = input.find(substring)
    while start >= 0 and n > 1:
        start = input.find(substring, start + 1)
        n -= 1
    return start

"""
Function find_year(): given a 10-K filepath in format "0001326801-13-000003", where the 
year is "13" between the two dashes, extract the year name
@ param filepath: string filepath containing the year
@ return: string of length 2 representing the final two digits of the year for a certain 10-K
"""
def find_year(filepath):
    start = filepath.find("10-K") + len("10-K")
    end = filepath.find("full-submission")
    filepath = filepath[start : end]
    return filepath[12 : 14]

"""
Function get_filings(): given the filepath to a specified directory (local), extract the names
of all files located in that folder (they will all be 10-K)
@ return: chronologically increasing list of sorted filenames 
"""
def get_filings():
    filepath = "/Users/anandkrishnan/Desktop/FSIL project/sec-edgar-filings/financial_statements"
    for root, dirs, files in os.walk(filepath):
        if '.DS_Store' in files:
            files.remove('.DS_Store')
        return sorted(files)

"""
Function read_write_one(): takes in filepath to downloaded (local) 10-K and extracts item 7a. from it,
writing to a new file in the "financial_statements" folder (also local)
@ param filepath: string filepath to the complete 10-K file
@ param company_name: ticker for company whose 10-K we are analyzing
void function, so no return value, but writes item 7a. to new file
"""
def read_write_one(filepath, company_name):
    with open(filepath, 'r') as f:
                
        # parse contents into a string
        contents = f.read()
        body_text = contents
        # newer 10-K files are in html format, so uses BeautifulSoup library to convert them to plaintext
        if body_text.find("<html>") != -1:
            soup = BeautifulSoup(contents, "html.parser")
            body_text = soup.body.get_text()

        # parsing data and extracting only risk analysis from the 10-K (assumes it is always Item 7a.)
        to_remove = ['\n', '\u00A0', ' '] # removing various characters that will interfere with string.find() method
        for char in to_remove:
            body_text = body_text.replace(char, " ")
        body_text = body_text.lower()

        # headings differ from company to company, but these are the 2 most standard wordings 
        # this is the primary area of improvement in this program, as some files differ in their naming format
        start = find_nth(body_text, "quantitative and qualitative disclosures about market risk", 2)
        if start == -1:
            start = find_nth(body_text, "quantitative and qualitative disclosures of market risk", 2)
        end = find_nth(body_text, "financial statements and supplementary data", 2)
        if end == -1:
            end = find_nth(body_text, "financial statements and supplemental data", 2)

        # only proceeds with writing if item 7a. properly extracted from original 10-K
        if start != -1 and end != -1:
            body_text = body_text[start : end] # condensing to 10-K
            
            if not len(body_text) > 10000: # remove oversize inputs that will eat up API tokens 

                # writing file to specific folder with naming format "{TICKER}{YEAR}"
                filename = company_name + find_year(filepath)
                file = open("/Users/anandkrishnan/Desktop/FSIL project/sec-edgar-filings/financial_statements/" + filename + ".txt", "w")
                file.write(body_text)
                file.close()

"""
Function read_write(): calls above function on all downloaded 10-K filings 
"""
def read_write():
    company_name = downloader.get_company() # calls function from earlier step to get user input
    base_path = "/Users/anandkrishnan/Desktop/FSIL project/sec-edgar-filings/" + company_name + "/10-K"

    # since the format is that files are downloaded into directory with a single 10-K folder containing
    # all filings, we have to extract the filings from that folder (base_path above)
    for root, dirs, files in os.walk(base_path):
        for directory in dirs:
            # Process each subfolder
            file_path = os.path.join(root, directory)
            file_path += "/full-submission.txt"

            read_write_one(file_path, company_name) # extracting item 7a. and writing to new folder
