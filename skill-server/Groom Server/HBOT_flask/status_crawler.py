##https://studyforus.com/share/584148

import time
import os
from selenium import webdriver
from PIL import Image
from io import BytesIO

filePath = 'images/'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('chromedriver',options=chrome_options)
driver.get('http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=11&ncvContSeq=&contSeq=&board_id=&gubun=')

# 전체 페이지의 사이즈를 구하여 브라우저의 창 크기를 확대하고 스크린캡처를 합니다.
page_width = driver.execute_script('return document.body.parentNode.scrollWidth')
page_height = driver.execute_script('return document.body.parentNode.scrollHeight')
driver.set_window_size(page_width, page_height)
png = driver.get_screenshot_as_png()

# 특정 element의 위치를 구하고 selenium 창을 닫습니다.
titles = driver.find_elements_by_class_name('s_title_in3')
tables = driver.find_elements_by_tag_name('table')
#
title1_location = titles[0].location
title1_size = titles[0].size
image1_location = tables[0].location
image1_size = tables[0].size
#
title2_location = titles[2].location
title2_size = titles[2].size
image2_location = tables[2].location
image2_size = tables[2].size
chart = driver.find_element_by_class_name('liveMoveChart')
chart_location = chart.location
chart_size = chart.size
driver.quit()

# 이미지를 element의 위치에 맞춰서 crop 하고 저장합니다.
im1 = Image.open(BytesIO(png))
left = image1_location['x']
top = title1_location['y']
right = title1_location['x'] + image1_size['width']
bottom = title1_location['y'] + image1_size['height'] + title1_size['height']+20
im1 = im1.crop((left, top, right, bottom))
#
im2 = Image.open(BytesIO(png))
left = image2_location['x']
top = title2_location['y']
right = title2_location['x'] + image2_size['width']
bottom = title2_location['y'] + image2_size['height'] + title2_size['height'] + chart_size['height']+20
im2 = im2.crop((left, top, right, bottom))
#
merged_height = image1_size['height'] + title1_size['height']+image2_size['height'] + title2_size['height'] + chart_size['height']+40
merged = Image.new('RGB', (image2_size['width'],merged_height))
merged.paste(im1, (0, 0))
merged.paste(im2, (0, image1_size['height'] + title1_size['height']+20))
merged.save(filePath+'status.png')