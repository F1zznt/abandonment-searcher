import requests
from bs4 import BeautifulSoup
import re

url = "http://hiddenside.ru/photos/industrial/russia.htm"
response = requests.get(url)
data = BeautifulSoup(response.text, "html.parser")
i = 0
links = []
for abandonment in data.find_all("p", class_="MsoNormal"):
    try:
        i += 1
        if i < 11:
            continue
        else:
            name = abandonment.span.find_all('span')
            link = abandonment.a["href"]
            links.append(link)

    except TypeError:
        break

city = input("Введите город с маленькой буквы по английски - kaliningrad, kaliningradskaya_obl: ")
pattern = re.compile(fr'{city}', re.IGNORECASE)


with open("abandonment.txt", "w") as abandonment_file:
    for link in links:
        if re.search(pattern, link):
            print(link)
            abandonment_file.write(link + "\n")
