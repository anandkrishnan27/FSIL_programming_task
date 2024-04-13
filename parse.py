from bs4 import BeautifulSoup
import downloader
import os

company_name = downloader.get_company()
base_path = "/Users/anandkrishnan/Desktop/FSIL project/sec-edgar-filings/" + company_name

for root, dirs, files in os.walk(base_path):
    for file in files:
        # Construct the full path to the file
        file_path = os.path.join(root, file)
        
        # Perform your operation on the file
        # For example, you can open and read the file
        with open(file_path, 'r') as f:
            # Perform your operation here
            # For example:
            file_contents = f.read()
            # Do something with the file contents

with open("/Users/anandkrishnan/Desktop/FSIL project/sec-edgar-filings/NVDA/10-K/0001012870-02-002262/full-submission.txt", "r", encoding="utf-8") as f:
    html_content = f.read()

# Parse HTML content
soup = BeautifulSoup(html_content, "html.parser")

# Extract text from body tag
body_text = soup.body.get_text()

# parsing data and extracting only selected financial statements from the 10-K (assumes they are always Item 6.)
body_text = body_text.replace("\n", "")
start = body_text.find("ITEM 6.")
end = body_text.find("ITEM 7.")
body_text = body_text[start : end]

file = open("/Users/anandkrishnan/Desktop/FSIL project/sec-edgar-filings/parsed_data1.txt", "w")
file.write(body_text)
file.close()

# selected financial data is what we need
# items 1A and 6
 
