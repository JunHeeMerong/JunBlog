from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def progarmmers(id,pw):
    try:
        noopen = webdriver.ChromeOptions()
        noopen.add_argument("headless")
        driver = webdriver.Chrome(options=noopen)

        url = 'https://programmers.co.kr/account/sign_in?referer=https://school.programmers.co.kr/learn/challenges?order=recent&page=1'
        driver.get(url)
        # driver.maximize_window() # 화면을 열고 풀스크린으로 적용
        id_box = driver.find_element(by=By.XPATH,value='//*[@id="main-app-account"]/div/div[2]/div/div[2]/div[1]/div/div[2]/div[2]/input')
        id_box.click()
        id_box.send_keys(id)

        pw_box = driver.find_element(by=By.XPATH,value='//*[@id="main-app-account"]/div/div[2]/div/div[2]/div[1]/div/div[2]/div[4]/input')
        pw_box.click()
        pw_box.send_keys(pw)

        login_box = driver.find_element(by=By.CSS_SELECTOR,value='#main-app-account > div > div.CqFgmmYa7JLTXOn9RZNl > div > div._i_cm82hE96w0g1ww1rO > div.by9dgl6a9xm729a_4ynt > div > div.G7QZ1shWGosDZ1csHsNt > button')
        login_box.click()
        time.sleep(1)

        score = driver.find_element(by=By.XPATH, value='//*[@id="edu-service-app-main"]/div/div[2]/article/div[2]/aside/div[1]/div/ul/li[2]/div[2]')
        # print('----------------')
        # print('점수 : ',score.text)
        return score.text
    except:
        # print('아이디/비밀번호가 잘못되었습니다.')
        return '아이디/비밀번호가 잘못되었습니다.'