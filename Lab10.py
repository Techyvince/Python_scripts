import string

def count_words(filepath):
    with open(filepath, 'r') as file:
        # Read the contents of the file and convert to lowercase
        content = file.read().lower()

        # Remove punctuation marks from the content
        content = content.translate(str.maketrans('', '', string.punctuation))

        # Split the content into words
        words = content.split()

        # Create a dictionary to store the word frequencies
        freq_dict = {}

        # Iterate over each word and update the frequency count in the dictionary
        for word in words:
            if word in freq_dict:
                freq_dict[word] += 1
            else:
                freq_dict[word] = 1

        # Return the dictionary of word frequencies
        return freq_dict

# Test the function with a sample text file
filepath = 'sample.txt'
word_freq = count_words(filepath)

# Display the word frequencies
for word, freq in word_freq.items():
    print(word, freq)
