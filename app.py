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

    # Process output if needed

    # Return the processed output
    return output[0]

if __name__ == "__main__":
    app.run(debug=True)