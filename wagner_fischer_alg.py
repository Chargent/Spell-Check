# Wagner-Fischer spell checking algorithm implementation in Python 
def load_dictionary(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

def wagner_fischer(w1, w2):
    len_w1, len_w2 = len(w1), len(w2)
    current_row = range(len_w1 + 1)
    for i in range(1, len_w2 + 1):
        previous_row, current_row = current_row, [i] + [0] * len_w1
        for j in range(1, len_w1 + 1):
            add, delete, change = previous_row[j] + 1, current_row[j-1] + 1, previous_row[j-1]
            if w1[j-1] != w2[i-1]:
                change += 1
            current_row[j] = min(add, delete, change)
    return current_row[len_w1]

def wf_spell_check(word, dictionary):
    suggestions = []
    for correct_word in dictionary:
        distance = wagner_fischer(word, correct_word)
        suggestions.append((correct_word, distance))
    suggestions.sort(key=lambda x: x[1])
    return suggestions[:10]


# Load dictionary
dictionary = load_dictionary("words.txt")

# Spell check execution
word = input("Enter a word: ").lower()
suggestions = wf_spell_check(word, dictionary)

# Print suggestions
print(f"Suggestions for '{word}':")
for suggested_word, distance in suggestions:
    print(f"{suggested_word} (Distance: {distance})")

