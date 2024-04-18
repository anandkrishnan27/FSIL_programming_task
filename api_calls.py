import downloader
import parse
from openai import OpenAI
from dotenv import load_dotenv

good_filings = parse.get_filings()
company = downloader.get_company()

def pick_years(filings, num_to_pick):
    final_list = []
    if len(filings) <= 0: return final_list

    step_size = len(filings) / (num_to_pick - 1)

    for i in range(num_to_pick - 1):
        index = int(i * step_size)
        final_list.append(filings[index])
    
    final_list.append(filings[len(filings) - 1])
    return final_list

filings_to_use = pick_years(good_filings, 7)

def generate_prompt(filings):
    prompt = ""
    filepath = "/Users/anandkrishnan/Desktop/FSIL project/sec-edgar-filings/financial_statements/"

    for filing in filings:
        current_filepath = filepath + filing

        with open(current_filepath) as f:
            contents = f.read()
            prompt += contents
            prompt += "\n\n"
    
    return prompt

filing_data = generate_prompt(filings_to_use)

load_dotenv()
client = OpenAI(api_key="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") # resolve how to store api key

primer = f"""You are a very confident, knowledgeable market analyst who can concisely analyze market risk factors affecting 
a company. Parse the below excerpts from {company}'s 10-K item 7a and answer the following questions. Item 7a over 
time for {company} is below.""" + '\n\n' + filing_data

results = []
questions = ["What are some possible macroeconomic factors that pose risk to this firm?"
             "Give a future outlook for this firm's risk profile", 
             "How risky are this firm's investments historically?", 
             "How should this company improve in order to lessen its risk profile?", 
             "Give me some matplotlib code that generates graphs with some visualization for this company."]

# priming message
completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": primer},
    ]
)

for question in questions:
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": question}
        ]
    )   

    results.append(completion.choices[0].message)

def get_results():
    return results

# should generate all text differently, so 5 different API calls to make a list with 5 elements that will be 
# passed into the app.py file


