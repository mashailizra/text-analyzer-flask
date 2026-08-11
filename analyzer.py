from collections import Counter


class UnsupportedFileTypeError(Exception):
    pass


class EmptyFileError(Exception):
    pass


class TextAnalyzer:
    def __init__(self, file_path, file_object=None):
        if not file_path.endswith(".txt"):
            raise UnsupportedFileTypeError("Only .txt files are supported.")

        self.file_path = file_path
        self.file_object = file_object

        if self.file_object is not None:
            self.file_object.seek(0)

            if self.file_object.read().strip() == b"":
                raise EmptyFileError("The file is empty.")

            self.file_object.seek(0)

        else:
            with open(self.file_path, "r") as file:
                if file.read().strip() == "":
                    raise EmptyFileError("The file is empty.")

    def read_lines(self):
        if self.file_object is not None:
            self.file_object.seek(0)

            for line in self.file_object:
                yield line.decode("utf-8")

        else:
            with open(self.file_path, "r") as file:
                for line in file:
                    yield line

    @property
    def word_count(self):
        count = 0

        for line in self.read_lines():
            count += len(line.split())

        return count

    @property
    def char_count(self):
        count = 0

        for line in self.read_lines():
            line = line.rstrip("\r\n")
            count += len(line)

        return count

    @property
    def sentence_count(self):
        count = 0

        for line in self.read_lines():
            count += line.count(".")
            count += line.count("!")
            count += line.count("?")

        return count

    def _get_words(self):
        words = []

        for line in self.read_lines():
            line = line.lower()
            line = line.replace(".", "")
            line = line.replace("!", "")
            line = line.replace("?", "")

            words.extend(line.split())

        return words

    @property
    def word_set(self):
        return set(self._get_words())

    

    def top_words(self, n=10):
        stopwords = {"the", "a", "an", "is", "and", "to", "of", "in"}

        words= self._get_words()

        filtered_words = filter(lambda word: word not in stopwords, words)
        word_counter = Counter(filtered_words)

        return word_counter.most_common(n)

print("Text Analyze Toolkit")

analyzer = TextAnalyzer("sample.txt")

print("Word count:", analyzer.word_count)
print("Character count:", analyzer.char_count)
print("Sentence count:", analyzer.sentence_count)
print("Top words:", analyzer.top_words())




