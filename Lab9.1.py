def pig_latin(sentence):
    words = sentence.split()
    pig_latin_words = []
    for word in words:
        pig_latin_word = word[1:] + word[0] + "ay"
        pig_latin_words.append(pig_latin_word)
    pig_latin_sentence = " ".join(pig_latin_words)
    return pig_latin_sentence.capitalize()

# Example usage
english_sentence = "I SLEPT MOST OF THE NIGHT"
pig_latin_sentence = pig_latin(english_sentence)
print(pig_latin_sentence) # Output: Iay leptsay ostmay foay hetay ightnay
