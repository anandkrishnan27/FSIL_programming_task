from sec_edgar_downloader import Downloader

AFTER_DATE = "1995-01-01"

entered_company = "COST"
def set_company(company):
    global entered_company
    entered_company = company

def get_company():
    return entered_company

def run():
    downloader = Downloader("Stanford University", "anandk12@stanford.edu", "/Users/anandkrishnan/Desktop/FSIL project")

    downloader.get("10-K", entered_company, after = AFTER_DATE)
