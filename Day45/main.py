from bs4 import BeautifulSoup

with open("Day45\website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
print(soup.title.string)  # This will print the title of the HTML document.
print(soup.prettify())  # This will print the HTML document in a more readable format.
print(soup.a)  # This will print the first anchor tag in the HTML document.
print(soup.find_all("a"))  # This will print all the anchor tags in the HTML document.
print(soup.find_all(name="a"))  # This will print all the anchor tags in the HTML document.
print(soup.find_all(class_="heading"))  # This will print all the elements with class "heading" in the HTML document.
print(soup.select("h1"))  # This will print all the h1 tags in the HTML document.
print(soup.select(".heading"))  # This will print all the elements with class "heading" in the HTML document.

all_anchor_tags = soup.find_all(name="a")  # This will find all anchor tags in the HTML document.

for tag in all_anchor_tags:
    print(tag.get("href"))  # This will print the href attribute of each anchor tag.

heading = soup.find(name="h1", id="name")  # This will find the h1 tag with id "name" in the HTML document.
print(heading.text)  # This will print the text of the heading.

name = soup.select_one("#name")  # This will select the element with id "name" in the HTML document.
print(name)  # This will print the element with id "name" in the HTML document.

soup.select_one(".heading")  # This will select the first element with class "heading" in the HTML document.
print(heading)