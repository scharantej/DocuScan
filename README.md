 ## Flask Application Design

### HTML Files

**1. index.html**
- This is the main HTML file that serves as the user interface for the application.
- It includes a form that allows users to upload a PDF document for analysis.
- The form should have a file input field and a submit button.

**2. results.html**
- This HTML file displays the results of the PDF analysis.
- It should include a table that lists the extracted entities and any violations of the predefined guidelines.

### Routes

**1. /**
- This route handles the GET request for the main page (index.html).

**2. /analyze**
- This route handles the POST request when the user submits the PDF document for analysis.
- It should call the appropriate Python function to perform the analysis and then redirect to the results page (results.html).

**3. /guidelines**
- This route handles the GET request for the page that displays the predefined guidelines or rules.
- It should display the guidelines in a clear and organized manner.

### Python Function

**1. analyze_pdf(pdf_file)**
- This function performs the analysis of the PDF document.
- It should extract the text from the PDF, identify and extract the specified entities, check the contents against the guidelines, and generate a report summarizing the results.

### Additional Considerations

- The application should handle errors gracefully, such as when a user uploads an invalid PDF file or when the analysis fails for some reason.
- The application should be well-structured and organized, with clear and concise code.
- The user interface should be intuitive and user-friendly, providing a seamless experience for the user.