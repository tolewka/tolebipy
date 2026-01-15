import string


input_file = "text.txt"
output_file = "analysis.txt"

line_count = 0
word_count = 0
word_frequency = {}


with open(input_file, "r", encoding="utf-8") as file:
    for line in file:
        line_count += 1

        
        line = line.lower()
        line = line.translate(str.maketrans("", "", string.punctuation))

        words = line.split()
        word_count += len(words)

        for word in words:
            if word in word_frequency:
                word_frequency[word] += 1
            else:
                word_frequency[word] = 1


with open(output_file, "w", encoding="utf-8") as file:
    file.write(f"Total number of lines: {line_count}\n")
    file.write(f"Total number of words: {word_count}\n")
    file.write("Word frequency:\n")

    for word, freq in word_frequency.items():
        file.write(f"{word}: {freq}\n")

print("Analysis completed. Results saved to analysis.txt")
