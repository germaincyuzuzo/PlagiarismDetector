Plagiarism Detector

This is a Python-based Plagiarism Detector application that analyzes and compares the content of two essays to identify potential plagiarism. It works by calculating the similarity between the word sets of the two documents and provides both a plagiarism percentage and detailed word analysis.

---

Features

Load and analyze two text files (`essay1.txt` and `essay2.txt`)
Identify and count common words across both essays
Search for specific words and show their frequency in each essay
Compute plagiarism percentage using word intersection and union
Report plagiarism if similarity ≥ 50%
Input validation and error handling for file and user input

---

Tech Stack

Python 3: Main programming language 
Standard Library Modules: re, collections.Counter, os, tabulate, PyPDF2

---

Project Structure

plagiarism_detector/
├── main.py # Main Python script
├── essay1.txt # First essay (input file)
├── essay2.txt # Second essay (input file)
└── README.md # Documentation

---

Setup Instructions

1. Clone the repository or download the files:

   git clone https://github.com/yourusername/plagiarism-detector.git
   cd plagiarism-detector

Create two text files in the same directory:

essay1.txt

essay2.txt

Run the program:

python detector.py

---

Example Usage
After running the script, you'll see:


Plagiarism Percentage: 56.78%
Potential Plagiarism Detected!


Common Words:
the - Essay1: 20, Essay2: 15
education - Essay1: 3, Essay2: 4
...


Enter a word to search (or 'exit' to quit):
education
'education' - Essay1: 3, Essay2: 4

---

How Plagiarism Is Calculated
The plagiarism percentage is calculated using the formula:


plagiarism % = (number of common words / total unique words) × 100
If plagiarism % ≥ 50%, the program reports potential plagiarism.

---

Input Validation & Error Handling

Checks if files exist and are not empty


Handles incorrect or empty user input


Ignores punctuation and case differences


