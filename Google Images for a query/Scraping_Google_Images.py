## Importing the vanilla libraries, and some which will help work in Google Colab

import requests
import urllib
import cv2
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from google.colab.patches import cv2_imshow
from urllib.request import Request, urlopen, urlretrieve
from bs4 import BeautifulSoup
from IPython.display import Image, display
from PIL import Image
from io import StringIO


## Installing and importing libraries important to the scraping work, such as Selenium

!pip install ipython
!pip install Selenium
!pip install parsel
import IPython
import selenium
import time
import parsel
import csv


## Building a Webdriver instance for Chrome using Selenium

!apt install chromium-chromedriver
!cp /usr/lib/chromium-browser/chromedriver /usr/bin
import sys
sys.path.insert(0,'/usr/lib/chromium-browser/chromedriver')
from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
wd = webdriver.Chrome('chromedriver',chrome_options=chrome_options)


## Importing some helpful modules and functions

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from parsel import Selector


## Taking the search query via a prompt

print("Enter the search term: ")
search = %sx read -p ""
print(search)


## Splitting the search query string and appending it into an array

search_length = 1
search_array = []
for x in search:
  search = x.split(' ')[:]
  for i in search:
    search_array.append(i)


## Creating the link which will be used for scraping

concatenator = "+".join(search_array)

base_link1 = "https://www.google.com/search?q="
base_link2 = "&source=lnms&tbm=isch&sa=X&ved=0ahUKEwj0qcvX8r_iAhXA8XMBHbQ1Dk8Q_AUIESgE&biw=1366&bih=605"

final_link = base_link1 + concatenator + base_link2
print(final_link)


## One method of scraping the link, using BeautifulSoup and Requests

# hdr = {'User-Agent': 'Mozilla/5.0'}
# req = Request(final_link,headers=hdr)
# page = urlopen(req)
# soup = BeautifulSoup(page, 'html.parser')
# # print(soup)


## Another method of scraping the link, using Selenium Webdriver (recommended)

wd.get(final_link)

html = wd.execute_script("return document.documentElement.innerHTML")
soup = BeautifulSoup(html)
# print(soup)


## One method of getting the image links from the webpage and displaying them to the console along with the corresponding images(recommended)

image = soup.find_all('img')
# print(image)
for im in list(image):
  image_src = im.get('data-src')
  if image_src:
#     print(image_src)
    
    img_data = requests.get(image_src).content
    with open('img.jpg', 'wb') as handler:
      handler.write(img_data)
      IPython.display.display(IPython.display.Image('img.jpg'))
    print(image_src)
    print("\n")


## Another method of getting the image links, this method even downloads the files and stores them

# image = soup.find_all('img')
# print(image)
# for im in list(image):
#   image_src = im.get('data-src')
#   if image_src:
#     print(image_src)
    
#     r = requests.get(image_src, stream = True)
#     downloaded_file = open("img.jpg", "wb")
#     for chunk in r.iter_content(chunk_size = 256):
#       if chunk:
#         downloaded_file.write(chunk)
#     IPython.display.display(IPython.display.Image("img.jpg"))
