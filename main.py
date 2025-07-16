import re
from collections import Counter
import PyPDF2
import os
from tabulate import tabulate 


# Load the content of a text or PDF file
def load_text(filename):
    if filename.endswith('.txt'):
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            print(f"File {filename} not found.")
            return ""
    elif filename.endswith('.pdf'):
        try:
            with open(filename, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                text = ""
                for page in reader.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text + "\n"
                return text
        except Exception as e:
            print(f"Error reading {filename}: {e}")
            return ""
    else:
        print(f"Unsupported file type: {filename}")
        return ""


# Convert text to lowercase, remove non-letter characters, and split into words
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    return text.split()


# Count occurrences of each word in a list
def get_word_counter(words):
    return Counter(words)


# Find words common to both essays and return their counts in each
def get_common_words(counter1, counter2):
    common = set(counter1) & set(counter2)
    return [(word, counter1[word], counter2[word]) for word in sorted(common)]


# Check if a word exists in either of the two essays
def search_word_exists(word, counter1, counter2):
    word = word.lower().strip()
    return word in counter1 or word in counter2


# Return the number of times a word appears in both essays
def search_word_counts(word, counter1, counter2):
    word = word.lower().strip()
    return counter1.get(word, 0), counter2.get(word, 0)


# Calculate the plagiarism percentage based on word overlap
def calculate_plagiarism_percentage(counter1, counter2):
    set1 = set(counter1)
    set2 = set(counter2)
    intersection = set1 & set2
    union = set1 | set2
    if not union:
        return 0.0
    return (len(intersection) / len(union)) * 100


# Print a formatted table of common words and their counts
def display_common_words_table(common_words):
    headers = ["Word", "Essay 1 Count", "Essay 2 Count"]
    print("\n--- Common Words ---")
    print(tabulate(common_words, headers=headers, tablefmt="grid"))


def main():
    essay1_path = input("Enter the path to Essay 1 (.txt or .pdf): ").strip()
    essay2_path = input("Enter the path to Essay 2 (.txt or .pdf): ").strip()

    text1 = clean_text(load_text(essay1_path))
    text2 = clean_text(load_text(essay2_path))

    if not text1 or not text2:
        print("One or both essays are empty or could not be read.")
        return

    counter1 = get_word_counter(text1)
    counter2 = get_word_counter(text2)

    plagiarism = calculate_plagiarism_percentage(counter1, counter2)
    print(f"\n Plagiarism Percentage: {plagiarism:.2f}%")
    if plagiarism >= 50:
        print("Potential Plagiarism Detected!")
    else:
        print("No Plagiarism Detected.")

    # Display common words
    common_words = get_common_words(counter1, counter2)
    if common_words:
        display_common_words_table(common_words)
    else:
        print("\nNo common words found.")

    # Word search loop
    while True:
        word = input("\n Enter a word to search (or 'exit' to quit): ").strip()
        if word.lower() == 'exit':
            print("Exiting program...")
            break
        elif not word:
            print("Please enter a non-empty word.")
            continue

        if search_word_exists(word, counter1, counter2):
            c1, c2 = search_word_counts(word, counter1, counter2)
            print(tabulate([[word, c1, c2]],
                           headers=["Word", "Essay 1", "Essay 2"],
                           tablefmt="fancy_grid"))
        else:
            print(f"'{word}' was not found in either essay.")

if __name__ == "__main__":
    main()
