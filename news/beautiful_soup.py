import requests
from bs4 import BeautifulSoup
from time import sleep
import fake_useragent
import json

user = fake_useragent.UserAgent().random
headers = {"user-agent": user}

url = "https://www.leaksbydaylight.com/category/news/"
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "lxml")
news_dict = {}


data = soup.find_all("header", class_="entry-header")
news_id = 0
#print(data)
for i in data:
    sleep(0.3)
    date = i.find("span", class_="item-metadata posts-date").text.replace("\n", "").replace(" ", "")
    title = i.find("div", class_="entry-header-details").find("h2").text
    pic = i.find("div", class_="post-thumbnail").find("img").get("data-src")
    descr = i.find("div", class_="post-excerpt").find("p").text
    link = i.find("div", class_="entry-header-details").find("h2").find("a").get("href")


    url_l = link
    response_l = requests.get(url_l, headers=headers)
    soup_l = BeautifulSoup(response_l.text, "lxml")

    data_l = soup_l.find_all("div", class_="elementor-widget-container")
    text = ""
    for i in data_l:
        try:
            text += i.find("span", class_="elementor-heading-title elementor-size-default").text.replace("'", "").replace("”", "").replace("’", "").replace("“", "").replace("é", "")
            if len(text) > 2999:
                text = text[:2999]
        except AttributeError:
            continue

    print(date)
    print(title)
    print(pic)
    print(descr)
    print(link)
    print(text + "\n\n")

    news_dict[news_id] = {
        "news_date_time": date,
        "news_title": title,
        "news_pictures": pic,
        "news_description": descr,
        "news_link": link,
        "news_text": text
    }
    news_id = news_id+1

    with open("news_dict.json", "w", encoding='windows-1251') as file:
        json.dump(news_dict, file, indent=4, ensure_ascii=False)

# with open('news_dict.json', 'r') as file:
#     data = json.load(file)
# print(data['1']['news_title'])

#python beautiful_soup.py