import requests
from bs4 import BeautifulSoup

URL="https://news.ycombinator.com/news"
content=requests.get(URL).text

web= BeautifulSoup(content, "html.parser")
print(web.prettify())
all_submissions= web.select(".athing")
all_links= []

for submission in all_submissions:
    id=submission.get("id")
    text=submission.select_one(".titleline a").get_text()
    link=submission.select_one(".titleline a").get("href")
    score=int(web.select_one(f"#score_{id}").get_text().replace(" points",""))
    all_links.append({"id":id,"link":link,"score":score,"text":text})

for link in all_links:
    print(link)

print(max([n["score"] for n in all_links]))




