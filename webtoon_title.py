from selenium import webdriver
import time

driver =  webdriver.Chrome('chromedriver.exe')
driver.get('https://comic.naver.com/webtoon/list.nhn?titleId=702672&weekday=tue')
time.sleep(2) #파이썬 코드를 잠시 멈춰줌

for i in range(5):
    titles = driver.find_elements_by_css_selector('td.title a')
    button = driver.find_element_by_css_selector('a.next')
    # elements와 element로 다름
    for title in titles:
        print(title.text)
    button.click()