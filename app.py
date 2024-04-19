from flask import Flask, render_template, request
import process_input

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process_text', methods=['POST'])
def process_text():
    # Retrieve user input from the request
    user_input = request.form['user_input']

    # Call your existing script with the user input
    output = process_input.main(user_input)
    print(output)
    
    questions = ["Macroeconomic Risks", "Future Risk Outlook", "Historical Risk", "Possible Improvements"]

    # for the purpose of testing
    file = open("/Users/anandkrishnan/Desktop/FSIL project/sec-edgar-filings/test.txt", "w")
    for message in output:
        file.write(message)
    file.close()

    data = zip(output, questions)
    # Return the processed output
    return render_template("result.html", output = output, ticker = user_input, data = data)

if __name__ == "__main__":
    app.run(debug=True)
