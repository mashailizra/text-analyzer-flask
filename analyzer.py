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
    @property
    def word_count(self):
        count=0

        for line in self.read_lines():
            count+=len(line.split())

        return count

    @property
    def char_count(self):
        count=0

        for line in self.read_lines():
            line=line.rstrip("\n")
            count+=len(line)

        return count

    @property
    def sentence_count(self):
        count=0

        for line in self.read_lines():
            count+=line.count(".")
            count+=line.count("!")
            count+=line.count("?")

        return count

    def top_words(self,n=10):
        words=[]

        stopwords ={"the","a","an","is","and","to","of","in"}

        for line in self.read_lines():
            line=line.lower()
            line=line.replace(".","")
            line=line.replace("!","")
            line=line.replace("?","")

            words.extend(line.split())

        filtered_words=filter(lambda word:word not in stopwords,words)
        word_counter=Counter(filtered_words)

        return word_counter.most_common(n)

    
print("Text Analysis Toolkit")

file_path = input("Enter the path of the text file: ")

try:
    analyzer = TextAnalyzer(file_path)

    print("Word count:", analyzer.word_count)
    print("Character count:", analyzer.char_count)
    print("Sentence count:", analyzer.sentence_count)
    print("Top words:", analyzer.top_words())

except UnsupportedFileTypeError:
    print("Error: Only .txt files are supported.")

except EmptyFileError:
    print("Error: The file is empty.")


