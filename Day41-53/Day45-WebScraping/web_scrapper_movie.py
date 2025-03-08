import requests
from bs4 import BeautifulSoup

URL= "https://www.empireonline.com/movies/features/best-movies-2/"
content= requests.get(URL).text
soup = BeautifulSoup(content, 'html.parser')

print(soup.prettify())

all_titles= [n.text for n in soup.select('span h2 strong')]
with open('movies.txt', 'w') as file:
    file.write('\n'.join(all_titles))

