from bs4 import BeautifulSoup
import requests
import json

with open("data.json", "r) as f:
    data = json.load(f)

base = "https://www3.nhk.or.jp/sokuho/jishin/data"

while True:
    r = requests.get(base + "/JishinReport.xml")
    soup = BeautifulSoup(r.text, "html.parser")
    url = item.get("url")
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    root = soup.find("Root")
    if data["last"] != root.find("Timestamp").text:
        image = base + "/" + root.find("Global")
        requests.post(data["webhook"], json={
            "embeds": [
              {
                  "title": "自身です",
                  "image": image
              }
            ]
        })
        data["last"] = root.find("Timestamp").text
        with open("data.json", "w") as f:
            json.dump(data, f)
