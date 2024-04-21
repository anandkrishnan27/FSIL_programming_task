"""
app.py contains functions that implement the Flask local web app that takes a user input of 
some stock ticker and call the LLM to generate insight based on its 10-K filings
"""
from flask import Flask, render_template, request
import process_input

app = Flask(__name__)

@app.route('/')
def index():
    # rendering the initial webpage with a form to enter a ticker
    return render_template("index.html")

@app.route('/process_text', methods=['POST'])
def process_text():
    # retrieve user input from the request
    user_input = request.form['user_input']

    # call functions that analyze 10-K correlating to the response
    output = process_input.main(user_input)

    # for testing purposes, downloades all API responses to a local text file 
    file = open("/Users/anandkrishnan/Desktop/FSIL project/sec-edgar-filings/test.txt", "w")
    for message in output:
        file.write(message)
    file.close()

    questions = ["Macroeconomic Risks", "Future Risk Outlook", "Historical Risk", "Possible Improvements"]
    data = zip(output, questions) # API output to be displayed on website "result.html" webpage
    
    # return the processed output to html page
    return render_template("result.html", output = output, ticker = user_input, data = data)

if __name__ == "__main__":
    app.run(debug=True)
