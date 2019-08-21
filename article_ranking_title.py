from selenium import webdriver
import time

driver =  webdriver.Chrome('chromedriver.exe')
driver.get('https://news.naver.com/main/ranking/popularDay.nhn?rankingType=popular_day&sectionId=103&date=20190526')
time.sleep(2) #파이썬 코드를 잠시 멈춰줌

titles = driver.find_elements_by_css_selector('div.ranking_headline a')
for title in titles:
    print(title.text)