from collections import Counter

print("Text Analysis Toolkit")
file_path =input("Enter the path of the text file:")

def read_lines(file_path):
    with open(file_path,"r")as file:
        for line in file:
            yield line

word_count=0
character_count=0
character_count_no_spaces=0
line_count=0
sentence_count=0

words =[]

for line in read_lines(file_path):
    line=line.rstrip("\n")

    clean_line= line.lower()
    clean_line= clean_line.replace(".","")
    clean_line= clean_line.replace("!","")
    clean_line= clean_line.replace("?","")

    line_words = clean_line.split()
    words.extend(line_words)

    line_count += 1
    word_count += len(line.split())
    character_count += len(line)
    character_count_no_spaces += len(line.replace(" ",""))
    sentence_count += line.count(".")
    sentence_count += line.count("!")
    sentence_count += line.count("?")

word_counter =Counter(words)


print("Word count:",word_count)
print("Character count:",character_count)
print("Character count without spaces:",character_count_no_spaces)
print("Line count:",line_count)
print("sentence count:",sentence_count)