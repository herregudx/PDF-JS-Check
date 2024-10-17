import os
import fitz  # PyMuPDF
import re

def check_for_javascript_in_pdf(directory):
    # Log file to record PDFs containing JavaScript
    with open("javascript_log.txt", "w") as log_file:
        # Walk through each file in the directory
        for root, _, files in os.walk(directory):
            for filename in files:
                if filename.lower().endswith('.pdf'):
                    file_path = os.path.join(root, filename)
                    try:
                        # Open the PDF file
                        pdf_doc = fitz.open(file_path)
                        
                        # Variable to store found JavaScript for current file
                        found_javascript = []
                        
                        # Search for JavaScript entries in the PDF
                        for page_num in range(pdf_doc.page_count):
                            page = pdf_doc[page_num]
                            # Extract text from the page to check for JavaScript-like patterns
                            page_text = page.get_text("text")
                            # Look for JavaScript patterns (basic detection)
                            if re.search(r'(?i)(javascript|eval|alert|document\.|window\.)', page_text):
                                found_javascript.append(page_text)
                        
                        # Check for embedded JavaScript (common in PDF files)
                        js_scripts = pdf_doc.get_js()
                        if js_scripts:
                            found_javascript.append(js_scripts)
                        
                        # If any JavaScript is found, print and log it
                        if found_javascript:
                            print(f"JavaScript found in {filename}:")
                            for js in found_javascript:
                                print(js)
                            
                            # Log the filename and JavaScript code to the file
                            log_file.write(f"JavaScript found in {filename}:\n")
                            for js in found_javascript:
                                log_file.write(f"{js}\n")
                            log_file.write("\n" + "-"*40 + "\n\n")

                    except Exception as e:
                        print(f"Error reading {file_path}: {e}")
                    finally:
                        # Close the PDF document
                        pdf_doc.close()

# Specify the directory path containing PDF files
directory_path = "/path/to/your/pdf/folder"
check_for_javascript_in_pdf(directory_path)
