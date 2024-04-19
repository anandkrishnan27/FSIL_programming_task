from openai import OpenAI
from dotenv import load_dotenv

def pick_years(filings, num_to_pick):
    final_list = []
    if len(filings) <= 0: return final_list

    step_size = len(filings) / (num_to_pick - 1)

    for i in range(num_to_pick - 1):
        index = int(i * step_size)
        final_list.append(filings[index])
    
    final_list.append(filings[len(filings) - 1])
    return final_list

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

results = []

def run_api(company, filing_data):
    load_dotenv()
    client = OpenAI(api_key="INSERT API KEY HERE")

    primer = f"""You are a very confident, knowledgeable, and specific market analyst who can analyze market risk factors
    affecting a company. Parse the below excerpts from {company}'s 10-K item 7a and answer the following questions. Item 7a over 
    time for {company} is below. Make sure your answers use {company}'s name and don't include bulleted/numbered lists.""" + '\n\n' + filing_data

    questions = ["What are some possible macroeconomic factors that pose risk to this firm?",
                "Give a future outlook for this firm's risk profile", 
                "How risky are this firm's investments historically?", 
                "How should this company improve in order to lessen its risk profile?", 
                "Give me some matplotlib code that generates specific graphs based on this data."]

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

    return results

# should generate all text differently, so 5 different API calls to make a list with 5 elements that will be 
# passed into the app.py file
