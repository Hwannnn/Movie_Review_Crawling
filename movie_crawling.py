# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import pandas as pd

def crawling(code, total_page):
    # url 조합
    front_url = "http://movie.naver.com/movie/point/af/list.nhn?st=mcode&sword="
    back_url = "&target=after&page="
    url_base = front_url + str(code) + back_url
    
    re = []
    for i in range(1, total_page + 1):
        url = url_base + str(i)
        
        res = requests.get(url)
        soup = BeautifulSoup(res.text, "lxml")
        
        score_result = soup.select(".list_netizen .title ")
        
        # 불필요한 텍스트 및 앞뒤 공백 제거
        for i in score_result:
            i.find(class_="movie").extract()
            i.find(class_="report").extract()
            re.append(i.text.strip())
    
    return re
            

    
def main():
    # 영화 고유코드와 긁어올 페이지 수
    code = 146485
    total_page = 20
    
    
    df = pd.DataFrame(crawling(code, total_page))
    print(df)
        
    df.to_csv('out.csv')


    
main()


