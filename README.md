# Text Analysis Toolkit
A Flask web app that analyzes uploaded .txt files: word/
character/sentence
counts, top words, and a Jaccard-similarity comparison between 
two documents.
## Status
Completed.
## Features
- Upload a `.txt` file and view word, character, and sentence counts plus the top 10 words
- Compare two `.txt` documents for word overlap using Jaccard similarity.
- Display shared words between two documents.
- Read uploaded files directly from memory without saving them to disk.
- Clean validation for empty files and unsupported file types.
- Friendly error messages using Flask flash messages.
- Simple shared CSS styling across all pages.
- Navigation between the Analyze and Compare pages.
## Tech stack
Python 3, Flask, HTML/CSS,Jinja templates
## Screenshots

### Analyze File
![Analyze File](screenshots/analyze.png)
### Analysis Results
![Analysis Results](screenshots/analysis-results.png)
### Compare Files
![Compare Files](screenshots/compare.png)
### Comparison Results
![Comparison Results](screenshots/comparison-results.png)

## How to Run

###
 1. Clone the repository

```bash
git clone <your-github-repository-url>
cd text-analyzer-flask

### 2.Create a virtual environment
python -m venv textanalyservervenv

### 3. activate the virtual environment 
.\textanalyservervenv\Scripts\Activate.ps1 #on windows powershell

### install dependencies
pip install -r requirements.txt

### start the flask application
flask --app app run
```
Then open http://127.0.0.1:5000 in your browser.
## What I learned- 
How a web request/response cycle works (routes, GET vs POST)- Reading uploaded files without saving them to disk- Rendering dynamic HTML with Jinja templates- Using sets for a real analytical task (similarity scoring).