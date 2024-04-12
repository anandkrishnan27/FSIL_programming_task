from sec_edgar_downloader import Downloader

AFTER_DATE = "1995-01-01"
COMPANIES = ["AMZN", "MSFT", "NVDA"]

downloader = Downloader("Stanford University", "anandk12@stanford.edu", "/Users/anandkrishnan/Desktop")

for company in COMPANIES:
    downloader.get("10-K", company, after = AFTER_DATE)