import downloader
import parse
import api_calls
import cleanup

def main(ticker):
    downloader.set_company(ticker)
    downloader.run()

    parse.read_write()
    filings = parse.get_filings()

    filings_to_use = api_calls.pick_years(filings, 7)
    prompt = api_calls.generate_prompt(filings_to_use)
    print(prompt)

    output = api_calls.run_api(ticker, prompt)
    cleanup.main()

    return output



