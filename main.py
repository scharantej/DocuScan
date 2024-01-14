 
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for
import PyPDF2
import re

# Create a Flask app
app = Flask(__name__)

# Define the main route
@app.route('/')
def index():
    return render_template('index.html')

# Define the route to handle PDF analysis
@app.route('/analyze', methods=['POST'])
def analyze():
    # Get the uploaded PDF file
    pdf_file = request.files['pdf_file']

    # Read the PDF file
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)

    # Extract text from the PDF file
    text = ""
    for page in pdf_reader.pages:
        text += page.extractText()

    # Identify and extract specific entities from the text
    entities = {
        'names': re.findall(r'[A-Z][a-z]+ [A-Z][a-z]+', text),
        'dates': re.findall(r'\d{1,2}/\d{1,2}/\d{4}', text),
        'locations': re.findall(r'[A-Z][a-z]+, [A-Z][a-z]+', text)
    }

    # Check the contents of the PDF against predefined guidelines
    violations = []
    for entity_type, entity_list in entities.items():
        for entity in entity_list:
            if entity in ['Confidential', 'Top Secret']:
                violations.append(f'{entity_type}: {entity}')

    # Generate a report summarizing the extracted entities and any violations
    report = {
        'entities': entities,
        'violations': violations
    }

    # Render the results page with the extracted entities and violations
    return render_template('results.html', report=report)

# Define the route to display the guidelines
@app.route('/guidelines')
def guidelines():
    return render_template('guidelines.html')

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
