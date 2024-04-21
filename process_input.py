"""
process_input.py contains functions that call the functions from downloader, parse, and api_calls
in sequence to execute the functionality of this web app. this main() function is used in app.py.
"""
import downloader
import parse
import api_calls
import cleanup

"""
Function main(): sequentially calls functions in imported files to download 10-K filings, then 
parse them and extract all item 7a. sections to a separate folder. Then, picks specific files to analyze, 
generates prompt for GPT API, actually calls API, extracts responses from JSON format, and deletes all 
downloaded files. 
@ param ticker: user-inputted stock ticker from app.py
@ return: list containing 5 API-generated responses to the questions from api_calls.py
"""
def main(ticker):
    # downloades files for passed company
    downloader.set_company(ticker)
    downloader.run()

    # extracts item 7a. for all 10-K
    parse.read_write()
    filings = parse.get_filings()

    # generates message to be sent to API
    filings_to_use = api_calls.pick_years(filings, 5)
    prompt = api_calls.generate_prompt(filings_to_use)

    # captures output from API, cleans it, and removes all files to save memory
    output = api_calls.run_api(ticker, prompt)
    content = [message.content for message in output]
    cleanup.main()

    return content




