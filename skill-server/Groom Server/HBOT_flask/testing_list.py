from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import json
from collections import OrderedDict

url_text = []
url_list = []
url = "https://govlab.eduwill.net/schedule/notice"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('chromedriver',options=chrome_options)
driver.get(url)

tab_list = driver.find_element_by_class_name("tab_list").find_elements_by_tag_name("li")

for btn in tab_list :
    btn.click()
    time.sleep(1)

    search = driver.find_element_by_css_selector("#contents > div > div > div > div > div > div > div.search_form > input[type=text]")
    search.send_keys("제주")
    search.send_keys(Keys.ENTER)
    time.sleep(3)

    link_num = driver.find_element_by_css_selector("#contents > div > div > div > div > div > div > div.table_wrap > table > tbody > tr:nth-child(1) > td:nth-child(1)").text
    page = driver.find_element_by_class_name("subject")
    url_text.append(page.find_element_by_tag_name('a').text)
    url_list.append(url+"/05/"+link_num)


driver.quit()


url_dict = []
for i in range(5) :
    tmp = {"title" : url_text[i], "link" : {"web" : url_list[i]}}
    url_dict.append(tmp)

file_data = OrderedDict()
file_data["items"] = url_dict

with open('testing_list.json', 'w', encoding="utf-8") as make_file:
    json.dump(file_data, make_file, ensure_ascii=False, indent="\t")

