import csv

all_Articles = []
with open("Articles.csv", encoding="utf8") as f:
    csvreader = csv.reader(f)
    data = list(csvreader)
    all_Articles = data[1:]

liked_Articles = []
disliked_Articles = []
