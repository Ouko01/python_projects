import string

def read_file(filename):
    """Read text file and return its contents."""
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{filename}' not found")
    except Exception as e:
        raise Exception(f"Error reading file: {str(e)}")

def clean_text(text):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    return text

def count_words(text):
    """Count ocurrences of each word in the text."""
    words = text.split()
    word_count = {}

    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    return word_count

def display_results(word_count):
    """Display word count results sorted by frequency."""
    sorted_counts = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

    print("\nWord Count Results: ")
    print("-" * 30)
    for word, count in sorted_counts:
        print(f"{word}: {count}")

def main():
    filename = input("Enter the name of the text file: ")
    
    try:
        # Read and process the file
        text = read_file(filename)
        text = clean_text(text)
        word_count = count_words(text)
    
        # Display results
        display_results(word_count)
        print(f"\nTotal unique words: {len(word_count)}")
    
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()