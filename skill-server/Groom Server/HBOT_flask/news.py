import os 
import sys 
import urllib.request 
#from urllib.parse import * 
import requests 
from bs4 import BeautifulSoup 
import json 
import re 

# 오픈 API 아이디, 비번 (최초 설정 후 건드리지 말 것) 
client_id = "nEur9Ya9AKmMw1zFEq64" 
client_secret = "BErFlH5jIu" 

keyword='코로나' 


display = 30  # 각 키워드 당 검색해서 저장할 기사 수

# # # 여기서부터는 코드입니다 (신경 안쓰셔도 됩니다!) 
# # # # Input(str) : 뉴스에 검색할 단어 넣기 
 
def news_search(min_name):

    #한글 인코딩
    encText = urllib.parse.quote(min_name) 

    #requset url 설정.
    # json url
    url = "https://openapi.naver.com/v1/search/news.json?query=" + encText + "&display=" + str(display) + "&sort=sim" 
    # xml url
    #url = "https://openapi.naver.com/v1/search/news.xml?query=" + encText 
    
    #requset 객체 생성 및 header에 api id 추가
    request = urllib.request.Request(url) 
    request.add_header("X-Naver-Client-Id",client_id) 
    request.add_header("X-Naver-Client-Secret",client_secret) 

    #response 객체 생성 
    response = urllib.request.urlopen(request) 
    #http 상태 코드
    rescode = response.getcode() 

    #rescod==200 은 성공 응답을 뜻함
    if(rescode==200): 

        #바이트 형식으로 가져와 UTF-8 형식으로 디코딩
        response_body_str = response.read().decode('utf-8') 
        json_acceptable_string = response_body_str.replace("'", "\"") 
        #json 파일 데이터 추출
        response_body = json.loads(response_body_str)

        title_link = {} 
        for i in range(0, len(response_body['items'])): 
            if i>=5:
                response_body['items'][i].pop('originallink',None)
            response_body['items'][i]["description"] = response_body['items'][i]["description"].replace("<b>","").replace("</b>","")
            response_body['items'][i]["title"] = response_body['items'][i]["title"].replace("<b>","").replace("</b>","").replace("&quot;","")
            
            response_body['items'][i].pop('originallink',None)
            response_body['items'][i].pop('pubDate',None)
            temp = response_body['items'][i]['link']
            response_body['items'][i]['link']={
                    'web':temp
            }
        with open('data.json','w', encoding='utf-8')as make_file:
            json.dump(response_body,make_file,ensure_ascii=False, indent="\t")
        return title_link
    else: 
            print("Error Code:" + rescode) 
        # 기사 제목 = 기사 링크 형태로 저장 
       

# 키워드 단일 검색
'''def keyword_search(keyword): 
    title_links = {} 
    for i in range(len(keyword)): 
        title_links.update(news_search(keyword))
    url_to_html(title_links)   
'''

if __name__ == '__main__': 
    news_search(keyword)
    

