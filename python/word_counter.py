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
    words = re.findall(r"\b\w+[-]*\w+\b", text)
    return words


def get_sentences(text):
    # Normalize line breaks
    text = re.sub(r"\n+", "\n", text)
    
    # Replace sentence-ending punctuation with a marker
    text = re.sub(r'[.!?]+(?:["\']?\s+|\s*$)', ' END ', text)

    # Treat standalone newlines as potential sentence breaks
    text = re.sub(r"\n", " END ", text)

    sentences = [s for s in text.split("END") if s.strip()]

    return sentences


def get_paragraphs(text):
    paragraphs = [p for p in text.split("\n\n") if p.strip()]
    return paragraphs


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

        sentences = get_sentences(text)
        total_sentences = len(sentences)
        print(f"Total sentences: {total_sentences}")

        paragraphs = get_paragraphs(text)
        total_paragraphs = len(paragraphs)
        print(f"Total paragraphs: {total_paragraphs}")