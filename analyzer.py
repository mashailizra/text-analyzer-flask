from collections import Counter


class UnsupportedFileTypeError(Exception):
    pass
class EmptyFileError(Exception):
    pass

class TextAnalyzer:
    def __init__(self, file_path):
        if not file_path.endswith(".txt"):
            raise UnsupportedFileTypeError("Only .txt files are supported.")

        with open(file_path, "r") as file:
            if file.read().strip() == "":
                raise EmptyFileError("The file is empty.")

        self.file_path = file_path

    def read_lines(self):
        with open(self.file_path, "r") as file:
            for line in file:
                yield line

analyzer = TextAnalyzer("sample.txt")
for line in analyzer.read_lines():
    print(line, end="")

print("\nText Analysis Toolkit")
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

stopwords = {"the","a","an","is","and","to","of","in"}


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

filtered_words= filter(lambda word: word not in stopwords,words)
filtered_counter= Counter(filtered_words)


print("Word count:",word_count)
print("Character count:",character_count)
print("Character count without spaces:",character_count_no_spaces)
print("Line count:",line_count)
print("sentence count:",sentence_count)

print("\nTop 10 most commomn words:")

for word,count in filtered_counter.most_common(10):
    print(word,":",count)