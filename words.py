import random
import twitter
import csv


auth = twitter.OAuth(consumer_key="XLGdm3hyV7o1LFxNcuaxGjIUL",
                     consumer_secret="gn3hQeqZP4kFhgE4bg7UT0HwlkKbGNvv0UPkEB4pZ8hwHKlEGY",
                     token="1262169625808105473-o3g2RV1BLU9VtBazpqclGTfQW63KGU",
                     token_secret="EsTaQuM35LJPXsso9Om7q3QfSaseiwlS9bxx7ayCoOnf7")

t = twitter.Twitter(auth=auth)


# しんやめリストから選ぶ
with open('bot/yameruna2.csv') as f:
    reader = csv.reader(f)
    box = []
    for row in reader:
        box.append(row)
max = len(box)
random = random.randrange(max)
kw = box[random][0]
waka = []
for i in kw:
    waka.append(i)
    if i == "！":
        waka.append('\n')
shindemo = "".join(waka)


# ツイートのみ
status = shindemo  # 投稿するツイート
t.statuses.update(status=status)  # Twitterに投稿

# * 0,2,6,8,10,12,14,16,18,20,22 * * * python /Users/pg3/Downloads/VSCODE/ann/ann.py
