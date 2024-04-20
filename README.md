# FSIL_programming_task

**Description**:
This project is a simple web application that accepts user input of a valid NYSE stock ticker (e.g., "NVDA", "JNJ", "BRK.B", etc.) and creates a dashboard with LLM-generated insight about the inputted company's risk profile based on its past 29 years of 10-K filings, specifically pertaining to item 7a. 

**Tech Stack:**
- Flask (web framework for app)
- Python (writing back-end functionality and calling LLM)
- HTML/CSS (creating front-end webpage and styling)
- sec_edgar_downloader API (downloading 10-K data from SEC website)
- OpenAI API (generating insight based on downloaded 10-K filings)

I used Flask because it was the simplest framework for this lightweight web application, especially considering the project backend was written in Python, and I didn't need any in-depth database functionality or user experience that would necessitate ReactJS. Otherwise, Python is the most familiar language to me and contained libraries that I was most familiar with (e.g., BeautifulSoup for HTML parsing, OpenAI, etc.), and I used it for this reason.

**Possible Improvements:**
- Runtime: This project takes a while (2ish minutes) to run, just owing to extracting all 10-K data and repeatedly parsing it/sending it to API, so optimization would be beneficial
- Graphs: As documented in the code, I called the LLM to generate matplotlib code that would create graphs in Python to display on the website, but the implementation for this functionality was outside my time availability, so I was unable to complete this task
- Deployment Online: Again owing to time constraints, I opted to just locally demo my app instead of deploying it online, but it would be beneficial to deploy it online if I had the time

**Project Installation**
The code in this repository is specific to my local desktop, so in order to have a functioning version, the user should download all files in this repository, change all file paths to the correct ones for their computer. Specifically, create a folder "FSIL project" for all this code, then within that a folder entiteld "sec-edgar-filings", and within that a folder entitled "financial_statements". An OpenAI API key is also necessary, so creating a free account and pasting a generated key into the string in api_calls.py "INSERT API KEY HERE" would cover this functionality.
