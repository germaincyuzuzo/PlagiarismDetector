import re
from collections import Counter

# Function to load and clean text 
def load_text(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return ""

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    words = text.split()
    return words

# Function to generate word frequency counters 
def get_word_counter(words):
    return Counter(words)

# Function to get common words 
def get_common_words(counter1, counter2):
    common = set(counter1) & set(counter2)
    result = []
    for word in common:
        result.append((word, counter1[word], counter2[word]))
    return result

# Function to search function that returns True/False 
def search_word_exists(word, counter1, counter2):
    word = word.lower().strip()
    return word in counter1 or word in counter2

# Function to return frequency counts if needed 
def search_word_counts(word, counter1, counter2):
    word = word.lower().strip()
    return counter1.get(word, 0), counter2.get(word, 0)

# Function to calculate plagiarism percentage 
def calculate_plagiarism_percentage(counter1, counter2):
    set1 = set(counter1)
    set2 = set(counter2)
    intersection = set1 & set2
    union = set1 | set2
    if not union:
        return 0.0
    return (len(intersection) / len(union)) * 100

# Function to run the main Program 
def main():
    # Load and preprocess essays
    essay1 = clean_text(load_text('essay1.txt'))
    essay2 = clean_text(load_text('essay2.txt'))

    if not essay1 or not essay2:
        print("One or both essays are empty or missing.")
        return

    counter1 = get_word_counter(essay1)
    counter2 = get_word_counter(essay2)

    # Calculate and display plagiarism percentage
    percentage = calculate_plagiarism_percentage(counter1, counter2)
    print(f"\nPlagiarism Percentage: {percentage:.2f}%")
    if percentage >= 50:
        print("Potential Plagiarism Detected!")
    else:
        print("No Plagiarism Detected.")

    # Display common words and their counts
    print("\nCommon Words:")
    common_words = get_common_words(counter1, counter2)
    if not common_words:
        print("No common words found.")
    else:
        for word, count1, count2 in common_words:
            print(f"{word} - Essay1: {count1}, Essay2: {count2}")

    # Word search loop with input validation
    while True:
        search = input("\nEnter a word to search (or 'exit' to quit): ").strip()
        if not search:
            print("Please enter a non-empty word.")
            continue
        if search.lower() == 'exit':
            break

        exists = search_word_exists(search, counter1, counter2)
        if not exists:
            print(f"The word '{search}' was not found in either essay.")
        else:
            count1, count2 = search_word_counts(search, counter1, counter2)
            print(f"'{search}' - Essay1: {count1}, Essay2: {count2}")

if __name__ == "__main__":
    main()
