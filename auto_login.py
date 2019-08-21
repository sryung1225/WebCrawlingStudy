from selenium import webdriver
import time

driver =  webdriver.Chrome('chromedriver.exe')
driver.get('https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com') #네이버 로그인창
time.sleep(0.5) #파이썬 코드를 잠시 멈춰줌

driver.find_element_by_css_selector('input#id').send_keys('*') #id가 'id'인 input에다가 send_key()값을 넣어라
time.sleep(1)
driver.find_element_by_css_selector('input#pw').send_keys('*')
time.sleep(1)
driver.find_element_by_css_selector('input.btn_global').click()
time.sleep(5)