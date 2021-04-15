from flask import Flask, jsonify

from Storage import all_Articles, liked_Articles, disliked_Articles
from Demographic_Filtering import output
from Content_Filtering import get_recommendations

app = Flask(__name__)


@app.route("/get-articles")
def getArticle():
    Article_Data = {
        "Title": all_Articles[0][12],
        "Article_Link": all_Articles[0][11],
        "Language": all_Articles[0][14],
        "Content_Id": all_Articles[0][4],
        "Event_Type": all_Articles[0][3],
        "Total_Events": all_Articles[0][15]
    }
    return jsonify({
        "data": Article_Data,
        "status": "success"
    })


@app.route("/liked-articles", methods={"POST"})
def likedArticle():
    Article = all_Articles[0]
    liked_Articles.append(Article)
    all_Articles.pop(0)
    return jsonify({
        "status": "success"
    })


@app.route("/disliked-articles", methods={"POST"})
def dislikedArticle():
    Article = all_Articles[0]
    disliked_Articles.append(Article)
    all_Articles.pop(0)
    return jsonify({
        "status": "success"
    })


@app.route("/popular-articles")
def popularArticles():
    article_data = []
    for article in output:
        temp_List = {
            "Title": article[0],
            "Article_Link": article[1],
            "Language": article[2],
            "Content_Id": article[3],
            "Event_Type": article[4],
            "Total_Events": article[5]
        }
        article_data.append(temp_List)
    return jsonify({
        "data": article_data,
        "status": "success"
    })


@app.route("/recommended-articles")
def recommendedArticles():
    all_recommended = []
    for liked_Article in liked_Articles:
        output = get_recommendations(liked_Article[4])
        for data in output:
            all_recommended.append(data)
    import itertools
    all_recommended.sort()
    all_recommended = list(all_recommended for all_recommended,
                           _ in itertools.groupby(all_recommended))
    article_data = []
    for recommended in all_recommended:
        temp_List = {
            "Title": recommended[0],
            "Article_Link": recommended[1],
            "Language": recommended[2],
            "Content_Id": recommended[3],
            "Event_Type": recommended[4],
            "Total_Events": recommended[5]
        }
        article_data.append(temp_List)
    return jsonify({
        "data": article_data,
        "status": "success"
    })


if (__name__ == "__main__"):
    app.run(debug=True)
