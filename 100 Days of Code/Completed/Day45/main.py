from bs4 import BeautifulSoup

with open("website.html", errors="ignore") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)  # title tag
# print(soup.title.name)  # Name of title tag is called title
# print(soup.title.string)  # Element content
# print(soup.prettify())  # Adds indents, encoding="utf-8" might not work for some reason
# print(soup.p)  # Can parse different elements, such as the first paragraph tag

# all_anchor_tags = soup.find_all(name="a")  # Can get all of a certain tag
#
# for tag in all_anchor_tags:
#     print(tag.getText())  # Use for loop to get the contents within those tags
#     print(tag.get("href"))  # This will return all the links in the anchor tags

# heading = soup.find(name="h1", id="name")
# print(heading)

# section_heading = soup.find(name="h3", class_="heading")  # 'class' will give a traceback as it is reserved for
# # creating a class in Python
# print(section_heading.get("class"))  # Will return the HTML class value


# company_url = soup.select_one(selector="p a")  # Can get to nested selectors
# print(company_url)

# name = soup.select_one(selector="#name")  # Can get the element from id called name
# print(name)

# headings = soup.select(".heading")  # Get a list of class called heading
# print(headings)
