import os
import traceback
import PyPDF2
import json

def read_file(file):
    """
    Reads the content of a file (PDF or TXT) and returns the text.
    """
    if file.name.endswith(".pdf"):
        try:
            # Use PdfReader instead of PdfFileReader
            pdf_reader = PyPDF2.PdfReader(file)
            text = ""

            # Iterate through all pages and extract text
            for page in pdf_reader.pages:
                page_text = page.extract_text()
                if page_text:  # Avoid adding None if page has no text
                    text += page_text

            return text

        except Exception as e:
            raise Exception('Error reading the PDF file')

    elif file.name.endswith(".txt"):
        # Read and decode text file
        return file.read().decode('utf-8')

    else:
        raise Exception('Unsupported file format. Only PDF and TXT files are supported.')

def get_table_data(quiz_str):
    """
    Converts quiz JSON string into a list of dictionaries for table display.
    """
    try:
        # Convert quiz string to dictionary
        quiz_dict = json.loads(quiz_str)
        quiz_table_data = []

        # Extract MCQ, options, and correct answer
        for key, value in quiz_dict.items():
            mcq = value.get('mcq', '')
            options = value.get('options', {})
            correct = value.get('correct', '')

            # Format options as "A -> option1 || B -> option2..."
            formatted_options = " || ".join(
                [f"{option} -> {option_value}" for option, option_value in options.items()]
            )

            quiz_table_data.append({
                'MCQ': mcq,
                'Choices': formatted_options,
                'Correct': correct
            })

        return quiz_table_data

    except Exception as e:
        traceback.print_exception(type(e), e, e.__traceback__)
        return False