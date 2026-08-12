from flask import Flask, render_template, request,flash
from analyzer import TextAnalyzer, EmptyFileError, UnsupportedFileTypeError

app = Flask(__name__)

app.secret_key="text-analysis-toolkit-secret"


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
        flash("Error: Only .txt files are supported.")
        return render_template("index.html")

    except EmptyFileError:
        flash("Error: The file is empty.")
        return render_template("index.html")
    
@app.route("/compare", methods=["GET", "POST"])
def compare():
    if request.method == "POST":
        file1 = request.files["file1"]
        file2 = request.files["file2"]

        try:
            analyzer1 = TextAnalyzer(
                file1.filename,
                file1.stream
            )

            analyzer2 = TextAnalyzer(
                file2.filename,
                file2.stream
            )

            words1 = analyzer1.word_set
            words2 = analyzer2.word_set

            common_words = words1 & words2
            union_words = words1 | words2

            similarity = (len(common_words) / len(union_words)) * 100

            return render_template(
                "compare_results.html",
                word_count1=analyzer1.word_count,
                word_count2=analyzer2.word_count,
                similarity=f"{similarity:.2f}",
                common_words=sorted(common_words)
            )

        except UnsupportedFileTypeError:
            flash("Error: Only .txt files are supported.")
            return render_template("compare.html")

        except EmptyFileError:
            flash("Error: One or both files are empty.")
            return render_template("compare.html")

    return render_template("compare.html")