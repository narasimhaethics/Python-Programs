def count_words(file_path):
    try:
        with open(file_path, 'r') as file:
            # Read the entire content of the file
            content = file.read()

            # Split the content into words using space as a delimiter
            words = content.split()

            # Count the number of words
            word_count = len(words)

            return word_count
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
file_path = 'example.txt'  # Replace with the path to your text file
result = count_words(file_path)

if result is not None:
    print(f"The number of words in the file '{file_path}' is: {result}")
