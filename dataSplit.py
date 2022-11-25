import random
from tqdm import tqdm

random.seed(1234)
random.shuffle(all_data)

def to_line(data):
    title = data["title"]
    body = data["body"]
    genre_id = data["genre_id"]

    assert len(title) > 0 and len(body) > 0
    return f"{title}\t{body}\t{genre_id}\n"

data_size = len(all_data)
train_ratio, dev_ratio,test_ratio = 0.7,0.15,0.15

with open(f"data/train.tsv","w",encoding="utf-8")as f_train,\
    open(f"data/dev.tsv","w",encoding="utf-8")as f_dev,\
    open(f"data/test.tsv","w",encoding="utf-8")as f_test:

    for i,data in tqdm(enumerate(all_data)):
        line = to_line(data)
        if i < train_ratio * data_size:
            f_train.write(line)
        elif i < (train_ratio + dev_ratio) * data_size:
            f_dev.write(line)
        else:
            f_test.write(line)