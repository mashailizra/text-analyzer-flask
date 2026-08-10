from flask import Flask, render_template, request
from analyzer import TextAnalyzer, EmptyFileError, UnsupportedFileTypeError

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    uploaded_file = request.files["file"]

    try:
        analyzer = TextAnalyzer(
            uploaded_file.filename,
            uploaded_file.stream
        )

        return render_template(
            "results.html",
            word_count=analyzer.word_count,
            char_count=analyzer.char_count,
            sentence_count=analyzer.sentence_count,
            top_words=analyzer.top_words()
        )

    except UnsupportedFileTypeError:
        return render_template(
            "index.html",
            error="Error: Only .txt files are supported."
        )

    except EmptyFileError:
        return render_template(
            "index.html",
            error="Error: The file is empty."
        )
