from selenium import webdriver
import time

driver =  webdriver.Chrome('chromedriver.exe')
driver.get('https://news.naver.com/main/ranking/popularDay.nhn?rankingType=popular_day&sectionId=103&date=20190526')
data=[]
time.sleep(2)

titles = driver.find_elements_by_css_selector('div.ranking_headline a')
title_l=[]
url_l=[]

for title in titles:
    title_l.append(title.text)
    url_l.append(title.get_attribute('href'))

for i in range(len(url_l)):
    comment_l=[]
    driver.get(url_l[i])
    time.sleep(0.5)
    comments = driver.find_elements_by_css_selector('div.u_cbox_text_wrap')
    for comment in comments:
        comment_l.append(comment.text)
    
    print("[",title_l[i],"]")
    time.sleep(0.5)
    for j in range(len(comment_l)):
        print("-",comment_l[j])
        print("")