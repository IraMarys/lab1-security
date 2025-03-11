import string
from collections import Counter

def caesar_cipher(text, shift, decrypt=False):
    
    alphabet = string.ascii_letters + string.digits + string.punctuation + " "
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]

    if decrypt:
        translation_table = str.maketrans(shifted_alphabet, alphabet)
    else:
        translation_table = str.maketrans(alphabet, shifted_alphabet)

    return text.translate(translation_table)

def frequency_analysis(text):
    
    total_chars = len(text)
    char_counts = Counter(text)
    
    return {char: count / total_chars for char, count in char_counts.items()}


with open("encrypted.txt", "r", encoding="utf-8") as file:
    encrypted_text = file.read()


frequencies = frequency_analysis(encrypted_text)


print("\nCharacter Frequencies (relative):")
for char, freq in sorted(frequencies.items(), key=lambda x: x[1], reverse=True):
    print(f"'{char}': {freq:.4f}")


most_common_char = max(frequencies, key=frequencies.get)


alphabet = string.ascii_letters + string.digits + string.punctuation + " "
assumed_space = " "


shift_guess = (alphabet.index(most_common_char) - alphabet.index(assumed_space)) % len(alphabet)

print(f"\nEstimated shift value: {shift_guess}")


decrypted_text = caesar_cipher(encrypted_text, shift_guess, decrypt=True)

print("\nDecrypted text:\n", decrypted_text)


with open("decrypted.txt", "w", encoding="utf-8") as file:
    file.write(decrypted_text)

print("\nDecryption complete! Check 'decrypted.txt'.")