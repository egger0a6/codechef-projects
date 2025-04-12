import re

def read_input_file(filename):
    try:
        # Open the file in read mode ('r')
        with open(filename, "r") as file:
        # Read the file content and strip any leading or trailing whitespaces
            content = file.read().strip()
        return content
    except FileNotFoundError:
        # Handle the case where the file does not exist
        print(f"Error: The file '{filename}' was not found.")
        # Return an empty string if the file is not found
        return ""


def get_words_split(text):
    # Split the text into words
    words = text.split()
    return words


def get_words_regex(text):
    # Use regex to extract words while ignoring punctuation  
    words = re.findall(r"\b\w+\b", text)
    return words

def word_frequency(words):
    search_word = input("Enter the word to search: ")
    word_freq = words.count(search_word)
    return word_freq, search_word


def display_results(total_words, search_word, word_frequency):
    print(f"Total Words: {total_words}")
    print(f"Frequency of '{search_word}': {word_frequency}")


if __name__ == "__main__":
    filename = 'text.txt'
    text = read_input_file(filename)
    
    if text:
        words = get_words_regex(text)
        total_words = len(words)
        word_freq, search_word = word_frequency(words)
        display_results(total_words, search_word, word_freq)