import string

def print_without_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    text_written_in_lowercase = text.lower()
    text_without_vowels = ''
    for character in text_written_in_lowercase:
        if character not in vowels:
            text_without_vowels += character
    print(text_without_vowels)

print_without_vowels('Upper')