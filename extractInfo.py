import tarfile
import re

target_genres = ["dokujo-tsushin",
                 "it-life-hack",
                 "kaden-channel",
                 "livedoor-homme",
                 "movie-enter",
                 "peachy",
                 "smax",
                 "sports-watch",
                 "topic-news"]

def remove_brackets(text):
    text = re.sub(r"(^【[^】]*】)|(【[^】]*】$)", "", text)
    return text

def normalize_text(text):
    assert "\n" not in text and "\r" not in text
    text = text.replace("\t", " ")
    text = text.strip()
    text = normalize_neologd(text)
    text = text.lower()
    return text

def read_title_body(file):
    next(file)
    next(file)
    title = next(file).decode("utf-8").strip()
    title = normalize_text(remove_brackets(title))
    body = normalize_text(" ".join([line.decode("utf-8").strip() for line in file.readlines()]))
    return title, body

genre_files_list = [[] for genre in target_genres]

all_data = []

with tarfile.open("ldcc-20140209.tar.gz") as archive_file:
    for archive_item in archive_file:
        for i, genre in enumerate(target_genres):
            if genre in archive_item.name and archive_item.name.endswith(".txt"):
                genre_files_list[i].append(archive_item.name)

    for i, genre_files in enumerate(genre_files_list):
        for name in genre_files:
            file = archive_file.extractfile(name)
            title, body = read_title_body(file)
            title = normalize_text(title)
            body = normalize_text(body)

            if len(title) > 0 and len(body) > 0:
                all_data.append({
                    "title": title,
                    "body": body,
                    "genre_id": i
                    })