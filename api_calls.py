import downloader
import parse
from openai import OpenAI
from dotenv import load_dotenv

good_filings = parse.get_filings()

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
print(filings_to_use)

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

input_string = generate_prompt(filings_to_use)
print(input_string)

load_dotenv()
client = OpenAI(api_key="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")

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)

print(completion.choices[0].message)


# You are a confident, knowledgeable market analyst who can concisely analyze market risk factors affecting a certain company
# Parse the below excerpts from {f string company's} 10-K item 7a and answer the following questions
# Item 7a over time for {insert company here}; {here}
# 1. What are some possible macroeconomic factors that pose risk to this firm?
# 2. Give a future outlook for this firm's risk profile
# 3. How risky are this firm's investments historically?
# 4. How should this company improve in order to lessen its risk profile?
# 5. Give me some matplotlib code that generates graphs with some visualization 


