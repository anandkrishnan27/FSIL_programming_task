from bs4 import BeautifulSoup
import downloader
import os

company_name = downloader.get_company()
base_path = "/Users/anandkrishnan/Desktop/FSIL project/sec-edgar-filings/" + company_name + "/10-K"
statement_number = 0

def find_nth(input, substring, n):
    start = input.find(substring)
    while start >= 0 and n > 1:
        start = input.find(substring, start + 1)
        n -= 1
    return start

for root, dirs, files in os.walk(base_path):
    for directory in dirs:
        # Process each subfolder
        file_path = os.path.join(root, directory)
        file_path += "/full-submission.txt"
        print(file_path)
        with open(file_path, 'r') as f:
            
            # parse contents into a string
            contents = f.read()
            body_text = contents
            if body_text.find("<html>") != -1:
                soup = BeautifulSoup(contents, "html.parser")
                body_text = soup.body.get_text()

            # parsing data and extracting only selected financial statements from the 10-K (assumes they are always Item 6.)
            to_remove = ['\n', '\u00A0', ' '] # removing various characters that will interfere with string.find() method
            for char in to_remove:
                body_text = body_text.replace(char, " ")
            body_text = body_text.lower()

            start = find_nth(body_text, "quantitative and qualitative disclosures about market risk", 2)
            if start == -1:
                start = find_nth(body_text, "quantitative and qualitative disclosures of market risk", 2)
            end = find_nth(body_text, "financial statements and supplementary data", 2)
            if end == -1:
                end = find_nth(body_text, "financial statements and supplemental data", 2)

            print(start)
            print(end)
            body_text = body_text[start : end]

            file = open("/Users/anandkrishnan/Desktop/FSIL project/sec-edgar-filings/financial_statements/" + company_name + str(statement_number) + ".txt", "w")
            file.write(body_text)
            file.close()

        statement_number += 1


 
