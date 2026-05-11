# Text Analyzer
# Count words
# Remove duplicates
# Convert to NATO alphabet

import pandas

file_path = "C:\\Users\\Lenovo\\classroom\\test_folder\\NATO_phonetic_alphabet.csv"

text = input("Enter text: ").upper()

word_list = text.split(" ") 
unique_list = list(set(word_list))

print(f"Total Words: {len(word_list)}")
print(f"\nUnique Words:\n{unique_list}")

print("\nNATO Conversion:\n")

data = pandas.read_csv(file_path)
new_dict = {row.letter: row.code for (index, row) in data.iterrows()}

for word in unique_list:
    nato_word = " ".join(new_dict[letter]for letter in word)
    print(f"{word} → {nato_word}")