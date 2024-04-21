"""
downloader.py contains functions that accomplish the downloading 10-K step of this process
"""
from sec_edgar_downloader import Downloader

AFTER_DATE = "1995-01-01"

entered_company = "COST" # base start company in case malfunction

"""
Function set_company(): set the company to be downloaded for to passed parameter
@ param company: entered company (user_input in app.py)
"""
def set_company(company):
    global entered_company
    entered_company = company

"""
Function get_company(): returns string of company ticker that we downloaded 10-K filings for
"""
def get_company():
    return entered_company

"""
Function run(): uses sec_edgar_downloader library to download all 10-K filings after 1995 for certain company
"""
def run():
    # creating user login and downloading files to local directory hardcoded in (another room for improvement) 
    downloader = Downloader("Stanford University", "anandk12@stanford.edu", "/Users/anandkrishnan/Desktop/FSIL project")
    downloader.get("10-K", entered_company, after = AFTER_DATE)
