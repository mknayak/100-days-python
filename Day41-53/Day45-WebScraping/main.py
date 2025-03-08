import bs4 as bs
import lxml

with open("./website.html") as file:
    content= file.read()

web= bs.BeautifulSoup(content, "html.parser")

print(web)
print(web.prettify())
print(web.title)  #first tag with name title

all_anchors = web.find_all("a")  #find all tags
print([n.string for n in all_anchors])
print([n.get("href") for n in all_anchors]) #get attribute value

heading_h3= web.find(name="h3",class_="heading") #class is reserve keyword, class_ is used to find by class name
print(web.select_one(selector="p a").get("href"))  #select,select_one are used to find my matching css selector

