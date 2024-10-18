# PDF-JS-Check
Checks for JavaScript in all PDF files in a given directory.

1. Go through each PDF file in a given directory.
2. Check for embedded JavaScript.
3. Print and log filenames and JavaScript code found in each PDF.

Requires PyMuPDF. Install with pip:
```
pip install pymupdf
```


### Explanation of "Warning: Bad xref":
You may encounter a warning message "Bad xref" when checking PDF's. This error usually occurs when accessing cross-reference entries and happens with corrupted or non-standard PDFs that don't properly handle cross-references.
