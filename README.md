# Text Analysis Toolkit
A Flask web app that analyzes uploaded .txt files: word/
character/sentence
counts, top words, and a two-document comparison feature.
## Status
In progress — Day 4/5 complete:comparison feature added.
## Tech stack
Python 3, Flask
## Features (growing daily)- 
- [x] CLI script: word/char/line/sentence counts, top 10 words.
- [x] Refactored to TextAnalyzer class with @property stats.
- [x] Custom EmptyFileError / UnsupportedFileTypeError.
- [x] Flask web app: upload a .txt file, view stats in the browser.
- [x] Compare two documents with Jaccard similarity 
(set intersection/union).