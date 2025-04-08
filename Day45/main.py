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