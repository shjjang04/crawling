from urllib.request import urlopen
from bs4 import BeautifulSoup
import pymysql
import urllib.error
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time



service = Service('C:\Downloads\chromedriver-win64') # 크롬 드라이버 다운받아서 위치 지정
options = webdriver.ChromeOptions()
driver = webdriver.Chrome()



conn = pymysql.connect(host='localhost', user='root', password='12345', db='moviedb', port=3306 , charset='utf8')

# Convert digital data to binary format

    
for i in range(70000, 170000, 100):
    cur = conn.cursor()
    movie = ["null" for i in range(13)]

    try:
        
        url =  ("https://movie.daum.net/moviedb/main?movieId=%d"% i)
        
        
        driver.get(url)
        

        search_box = driver.find_element(By.XPATH, '//*[@id="mainContent"]/div/div[2]/div[1]/ul/li[1]/a/span')
        actions = webdriver.ActionChains(driver).move_to_element(search_box)
        actions = webdriver.ActionChains(driver).click(search_box)
        # time.sleep(1)
        actions.perform()
        
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        # response = urlopen(url)
        # soup = BeautifulSoup(response, "html.parser")
        
        
        director = soup.select('div>strong')[9].text
        print(director)
        
        # director = soup.find_all('div','thumb_cont')
        # print(director)
        
        # sql = "INSERT INTO movie (m_name, m_opening, m_reopening, m_genre, m_nation, m_age, m_runtime, m_grade, m_attendance, m_awards, m_director, m_actor) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

        # val = (movie[0], movie[1], movie[2], movie[3], movie[4], movie[5], movie[6], movie[7], movie[8], movie[9], movie[10], movie[11])
        # print("%d번째" % i)
        # cur.execute(sql, val)
        # conn.commit()
        
    except:
            print("%d 번째에서 오류" % i)
            pass