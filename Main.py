from flask import Flask, jsonify
import csv

app = Flask(__name__)

all_Articles = []
liked_Articles = []
disliked_Articles = []

with open("Articles.csv", encoding="utf8") as f:
    csvreader = csv.reader(f)
    data = list(csvreader)
    all_Articles = data[1:]


@app.route("/get-articles")
def getArticle():
    return jsonify({
        "data": all_Articles[0],
        "status": "success"
    })


@app.route("/liked-articles", methods={"POST"})
def likedArticle():
    global all_Articles
    Article = all_Articles[0]
    all_Articles = all_Articles[1:]
    liked_Articles.append(Article)
    return jsonify({
        "status": "success"
    })


@app.route("/disliked-articles", methods={"POST"})
def dislikedArticle():
    global all_Articles
    Article = all_Articles[0]
    all_Articles = all_Articles[1:]
    disliked_Articles.append(Article)
    return jsonify({
        "status": "success"
    })


if (__name__ == "__main__"):
    app.run(debug=True)
