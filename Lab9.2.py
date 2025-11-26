def count_vowels(string):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    for char in string:
        if char in vowels:
            vowel_count += 1
    return vowel_count

def count_consonants(string):
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    consonant_count = 0
    for char in string:
        if char in consonants:
            consonant_count += 1
    return consonant_count

# Get input from user
input_string = input("Enter a string: ")

# Count vowels and consonants
vowel_count = count_vowels(input_string)
consonant_count = count_consonants(input_string)

# Print results
print("The string contains", vowel_count, "vowels and", consonant_count, "consonants.")
