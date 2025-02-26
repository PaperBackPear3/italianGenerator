import json

# Read the JSON file
with open(
    "italian-dictionary/dictionary_sorted.json", "r", encoding="utf-8"
) as json_file:
    data = json.load(json_file)

# Extract words
words = [entry["word"] for entry in data]

# Write words to a text file
with open("words.txt", "w", encoding="utf-8") as txt_file:
    for word in words:
        txt_file.write(word + "\n")
