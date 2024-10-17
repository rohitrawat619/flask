import PyPDF2
import language_tool_python
from fpdf import FPDF

# Function to read PDF content
def read_pdf(file_path):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text

# Function to correct grammar using LanguageTool
def correct_grammar(text):
    tool = language_tool_python.LanguageTool('en-US')  # You can use 'en-GB' for British English
    matches = tool.check(text)
    corrected_text = language_tool_python.utils.correct(text, matches)
    return corrected_text

# Function to save corrected text as a new PDF
def save_as_pdf(text, output_pdf_path):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)
    
    # Split the text into lines for better PDF formatting
    for line in text.split('\n'):
        pdf.multi_cell(0, 10, line)
    
    pdf.output(output_pdf_path)

# Main script
pdf_file_path = 'rohit-rawat-resume.pdf'  # Replace with your input PDF file path
output_pdf_path = 'corrected_output.pdf'  # Output path for the corrected PDF

# Read the original PDF
pdf_text = read_pdf(pdf_file_path)

# Correct the grammar
corrected_text = correct_grammar(pdf_text)

# Save the corrected text into a new PDF
save_as_pdf(corrected_text, output_pdf_path)

print("Grammar correction completed and saved to", output_pdf_path)