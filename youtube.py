# from bs4 import BeautifulSoup
# import requests

# response = requests.get("https://www.youtube.com/@kurzgesagt/videos")
# soup = BeautifulSoup(response.text, "html.parser")

# print(soup.find("a"))
# x = soup.find_all(attrs={"class": "text"})
# for tag in x:
#     print(tag["href"])
# for y in x:
#     # z = (soup.find_all("span")[1])
#     print(y)
#     z = (soup.find_all(attrs={"class": "text"})[y].get_text)
#     if "success" in z: 
#         print(z)






# x =(soup.find_all("span")[1])
# def has_word(tag, word):
#     return tag and word in tag

# print(soup.find_all(has_word("quote", "success")))

# for y in len(x):
#     z = (soup.find_all("span")[1])
# print(soup.find_all(attrs={"class": "quote"}))

# print(soup.select(".quote"))=-

# import pandas as pd
# pd.set_option('max_colwidth',-1)

# from bs4 import BeautifulSoup as bs
# import requests

# my_url = "https://www.youtube.com/user/aandawesome/videos"

# r = requests.get(my_url)
# page = (r.text)
# soup=bs(page,'html.parser')

# d = []
# for match in soup.find_all('div',class_="yt-lockup-content"):
#     view = match.find('ul',class_="yt-lockup-meta-info")
#     d.append(
#         {
#             'Title': match.a.text,
#             'View': view.text.split("views")[0],
#             'Upload date':view.text.split("views")[1]
#         }
#     )

# pd.DataFrame(d)

# from selenium import webdriver

# def get_channel_results():
#     driver = webdriver.Chrome()
#     driver.get('https://www.youtube.com/results?search_query=mojang')

#     title = driver.find_element_by_css_selector('#info #text').text
#     link = driver.find_element_by_css_selector('#main-link').get_attribute('href')
#     subs = driver.find_element_by_css_selector('#subscribers').text
#     video_count = driver.find_element_by_css_selector('#video-count').text
#     desc = driver.find_element_by_css_selector('#description').text
#     print(f'{title}\n{link}\n{subs}\n{video_count}\n{desc}')

# get_channel_results()

# # output:
# '''
# Minecraft
# https://www.youtube.com/user/TeamMojang
# 7.4M subscribers
# 542 videos
# This is the official YouTube channel of Minecraft. We tell stories about the Minecraft Universe. ESRB Rating: Everyone 10+ with ...
# '''

# from selenium import webdriver

# from selenium.webdriver.chrome.service import Service

# from selenium.webdriver.support.ui import WebDriverWait

# from selenium.webdriver.support import expected_conditions as EC

# from bs4 import BeautifulSoup

# import codecs

# import re

# from webdriver_manager.chrome import ChromeDriverManager


# driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))


# val = input("Enter a url: ")

# wait = WebDriverWait(driver, 10)

# driver.get(val)


# get_url = driver.current_url
# wait.until(EC.url_to_be(val))


# if get_url == val:


#     page_source = driver.page_source


# soup = BeautifulSoup(page_source,features="html.parser")
# keyword=input("Enter a keyword to find instances of in the article:")
# matches = soup.body.find_all(string=re.compile(keyword))

# len_match = len(matches)

# title = soup.title.text

# print("got this far")


# file=codecs.open("article_scraping.txt", "a+")

# file.write(title+"\n")

# file.write("The following are all instances of your keyword:\n")

# count=1

# for i in matches:

#     file.write(str(count) + "." +  i  + "\n")

#     count+=1

# file.write("There were “+str(len_match)+” matches found for the keyword.")

# file.close()

# driver.quit()

# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options

# options = Options()
# options.headless = True
# options.add_argument("--window-size=1920,1200")

# driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
# driver.get("https://www.nintendo.com/")
# print(driver.page_source)
# driver.quit()

# from bs4 import BeautifulSoup
# from urllib import request
# import requests
# import json
# link = "https://www.youtube.com/@LackadaisyComic" 
# response = requests.get(link)
# soup = BeautifulSoup(response.text, 'html.parser')
# html = request.urlopen(link).read()
# # site_json=json.loads(soup.text)
# # print(site_json)
# print(soup.prettify())
# print(soup.title.string)

# from urllib import request
# from bs4 import BeautifulSoup
# import json
# url = 'http://mygene.info/v3/query?q=symbol:CDK2&species:human&fields=name,symbol,entrezgene'
# html = request.urlopen(url).read()
# soup = BeautifulSoup(html,'html.parser')
# site_json=json.loads(soup.text)
# #printing for entrezgene, do the same for name and symbol
# print([d.get('entrezgene') for d in site_json['hits'] if d.get('entrezgene')])

# from bs4 import BeautifulSoup
# import requests
# import re
# import json

# url = "https://www.youtube.com/@LackadaisyComic/about"

# soup = BeautifulSoup(requests.get(url, cookies={"CONSENT": "YES+1"}).text, "html.parser")

# data = re.search(r"var ytInitiaData = ({.*});", str(soup.prettify())).group(1)

# json_data = json.loads(data)

# channel_id = json_data["header"]["c4TabbedHeaderRender"]["channelid"]
# # import re
# import jsonf
# import requests
# from bs4 import BeautifulSoup

# URL = "https://www.youtube.com/c/Rozziofficial/about"
# soup = BeautifulSoup(requests.get(URL).content, "html.parser")

# # We locate the JSON data using a regular-expression pattern
# data = re.search(r"var ytInitialData = ({.*});", str(soup)).group(1)

# # Uncomment to view all the data
# # print(json.dumps(data))

# # This converts the JSON data to a python dictionary (dict)
# json_data = json.loads(data)

# # This is the info from the webpage on the right-side under "stats", it contains the data you want
# stats = json_data["contents"]["twoColumnBrowseResultsRenderer"]["tabs"][5]["tabRenderer"]["content"]["sectionListRenderer"]["contents"][0]["itemSectionRenderer"]["contents"][0]["channelAboutFullMetadataRenderer"]

# print("Channel Views:", stats["viewCountText"]["simpleText"])
# print("Joined:", stats["joinedDateText"]["runs"][1]["text"])


from pytube import YouTube
video_url = input("to start following a channel please insert a video link from the channel:>")
x = YouTube(video_url)
print("channel id:>",x.channel_id)
print("channel url:>",x.channel_url)