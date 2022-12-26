from unittest import result
import telegram
import requests
from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters
from bs4 import BeautifulSoup 
from selenium import webdriver
import urllib.request as req
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

API_key='knI%2FsEhuhoIf37FOmsc8uCq6qdcCXaJU9%2BKHEwgtLzMWGJ7A7LtC3w3Z3JvKzcE4cSrxn6reCcJi2FzIcKvKAQ%3D%3D'
 
options = webdriver.ChromeOptions() 
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
driver  = webdriver.Chrome("C:\\Users\\dbtmd\\PycharmProjects\\pythonProject\\chromedriver.exe", options = options) 
#확진자 검색 후 코로나 확진자 수 정보 컴포넌트 위치 파악 후 크롤링
def covid_num_crawling():
    code = req.urlopen("https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%ED%99%95%EC%A7%84%EC%9E%90")
    #html 방식으로 파싱
    soup = BeautifulSoup(code, "html.parser")
    #정보 get
    #info_num = soup.select("div.title_wrap dd.desc _y_first_value")
    info_num = soup.select("div.status_info em")
    result = info_num[0].string #=> 확진자 나중에 확인할 것.
    return result

# 국외(미국) 코로나 확진자 (나라_명)
def covid_nation_news():
    code = req.urlopen("http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=14&ncvContSeq=&contSeq=&board_id=&gubun=")
    soup = BeautifulSoup(code, "html.parser")
    nation_num = soup.select("tr:nth-of-type(48) td:nth-of-type(1)")
    nation_re = nation_num[0].string
    return nation_re

# 국외(미국) 코로나 확진자 (확진자_명)
def covid_nation_case():
    code = req.urlopen("http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=14&ncvContSeq=&contSeq=&board_id=&gubun=")
    soup = BeautifulSoup(code, "html.parser")
    nation_t = soup.select("tr:nth-of-type(48) td:nth-of-type(2)")
    nation_confinrmed = nation_t[0].string
    return nation_confinrmed

# 국외(2번째) 코로나 확진자 (나라_명)
def covid_nation_news2():
    code = req.urlopen("http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=14&ncvContSeq=&contSeq=&board_id=&gubun=")
    soup = BeautifulSoup(code, "html.parser")
    nation_num2 = soup.select("tr:nth-of-type(5) td:nth-of-type(1)")
    nation_re2 = nation_num2[0].string
    return nation_re2

# 국외(2번째) 코로나 확진자 (확진자_명)
def covid_nation_case2():
    code = req.urlopen("http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=14&ncvContSeq=&contSeq=&board_id=&gubun=")
    soup = BeautifulSoup(code, "html.parser")
    nation_t2 = soup.select("tr:nth-of-type(5) td:nth-of-type(2)")
    nation_confinrmed2 = nation_t2[0].string
    return nation_confinrmed2

# 국외(3번째) 코로나 확진자 (나라_명)
def covid_nation_news3():
    code = req.urlopen("http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=14&ncvContSeq=&contSeq=&board_id=&gubun=")
    soup = BeautifulSoup(code, "html.parser")
    nation_num3 = soup.select("tr:nth-of-type(1) td:nth-of-type(1)")
    nation_re3 = nation_num3[0].string
    return nation_re3

# 국외(3번째) 코로나 확진자 (확진자_명)
def covid_nation_case3():
    code = req.urlopen("http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=14&ncvContSeq=&contSeq=&board_id=&gubun=")
    soup = BeautifulSoup(code, "html.parser")
    nation_t3 = soup.select("tr:nth-of-type(1) td:nth-of-type(2)")
    nation_confinrmed3 = nation_t3[0].string
    return nation_confinrmed3

#국내 최신 코로나 뉴스
def covid_news_crawling():
    code = req.urlopen("https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EC%BD%94%EB%A1%9C%EB%82%98")
    soup = BeautifulSoup(code, "html.parser")
    title_list = soup.select("a.news_tit")
    output_result = ""
    for i in title_list:
        title = i.text
        news_url = i.attrs["href"]
        output_result += title + "\n" + news_url + "\n\n"
        if title_list.index(i) == 2:
            break
    return output_result
 
def covid_image_crawling(image_num=5):
    if not os.path.exists("./코로나이미지"):
        os.mkdir("./코로나이미지")
 
    browser = webdriver.Chrome("./chromedriver")
    browser.implicitly_wait(3)
    wait = WebDriverWait(browser, 10)
 
    browser.get("https://search.naver.com/search.naver?where=image&section=image&query=%EC%BD%94%EB%A1%9C%EB%82%98&res_fr=0&res_to=0&sm=tab_opt&color=&ccl=0&nso=so%3Ar%2Cp%3A1d%2Ca%3Aall&datetype=1&startdate=&enddate=&gif=0&optStr=d&nq=&dq=&rq=&tq=")
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.photo_group._listGrid div.thumb img")))
    img = browser.find_elements_by_css_selector("div.photo_group._listGrid div.thumb img")
    for i in img:
        img_url = i.get_attribute("src")
        req.urlretrieve(img_url, "./코로나이미지/{}.png".format(img.index(i)))
        if img.index(i) == image_num-1:
            break
    browser.close()

# 코로나 지원정책 이미지 크롤링
def covid_image_support_policy(image_num=5):
    if not os.path.exists("./코로나지원정책"):
        os.mkdir("./코로나지원정책")
 
    browser = webdriver.Chrome("./chromedriver")
    browser.implicitly_wait(3)
    wait = WebDriverWait(browser, 10)
 
    browser.get("https://www.google.com/search?q=%EC%BD%94%EB%A1%9C%EB%82%98+%ED%94%BC%ED%95%B4%EC%A7%80%EC%9B%90%EC%A0%95%EC%B1%85&sxsrf=ALiCzsaOspcDQLchxeyBZfglWjh1qpVQZw:1654506124415&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiw8MvOu5j4AhUgo1YBHYPCBOIQ_AUoAnoECAEQBA&biw=1536&bih=714&dpr=1.25")
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.bRMDJf img")))
    img = browser.find_elements_by_css_selector("div.bRMDJf img")
    for i in img:
        img_url = i.get_attribute("src")
        req.urlretrieve(img_url, "./코로나지원정책/{}.png".format(img.index(i)))
        if img.index(i) == image_num-1:
            break
    browser.close()
 
 

#토큰 넘버
token = "5226796928:AAEkH-Trb9xv0IdNdT5FQwzHzeUb8OwGuu8"
id = "5207755743"
 
bot = telegram.Bot(token)
info_message = '''- 오늘 확진자 수 확인 : "코로나" 입력하세요.
- 코로나 관련 뉴스 : "뉴스" 입력하세요.
- 코로나 관련 이미지 : "이미지" 입력하세요.
- 코로나 국외 상황 확인 : "국외발생현황" 입력하세요.
- 코로나 피해지원정책 확인 : "피해지원정책" 입력하세요.
'''
nation_message = '''- 현재 코로나 확진자수를 알고 싶은 나라를 입력하세요.'''

policy_message = ''' 가장 최근 3가지의 피해지원정책을 알려드리겠습니다. '''

bot.sendMessage(chat_id=id, text=info_message)

updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher
updater.start_polling()
 
### 챗봇 답장
def handler(update, context):
    user_text = update.message.text # 사용자가 보낸 메세지를 user_text 변수에 보내기.
    # 오늘 확진자 수 답장
    if (user_text == "코로나"):
        covid_num = covid_num_crawling()
        bot.send_message(chat_id=id, text="오늘 확진자 수 : {} 명".format(covid_num))
        bot.sendMessage(chat_id=id, text=info_message)
    # 코로나 관련 뉴스 답장
    elif (user_text == "뉴스"):
        covid_news = covid_news_crawling()
        bot.send_message(chat_id=id, text=covid_news)
        bot.sendMessage(chat_id=id, text=info_message)
    elif (user_text == "국외발생현황"):
        # 첫 번째
        covid_nation = covid_nation_news()
        covid_case = covid_nation_case()
        # 두 번째
        covid_nation2 = covid_nation_news2()
        covid_case2 = covid_nation_case2()
        # 세 번째
        covid_nation3 = covid_nation_news3()
        covid_case3 = covid_nation_case3()

        bot.send_message(chat_id=id, text="현재 {}의 확진자 수는 : {}\n현재 {}의 확진자 수는 : {}\n현재 {}의 확진자 수는 : {}".format(covid_nation, covid_case, covid_nation2, covid_case2, covid_nation3, covid_case3))
        bot.sendMessage(chat_id=id, text=info_message)
            

    # 코로나 관련 이미지 답장
    elif (user_text == "이미지"):
        bot.send_message(chat_id=id, text="최신 이미지 가져오는 중...")
        covid_image_crawling(image_num=10)
        # 이미지 한장만 보내기
        # bot.send_photo(chat_id=id, pho"to=open("./코로나이미지/0.png", 'rb'))
        # 이미지 여러장 묶어서 보내기
        photo_list = []
        for i in range(len(os.walk("./코로나이미지").__next__()[2])): # 이미지 파일 개수만큼 for문 돌리기
            photo_list.append(telegram.InputMediaPhoto(open("./코로나이미지/{}.png".format(i), "rb")))
        bot.sendMediaGroup(chat_id=id, media=photo_list)
        bot.sendMessage(chat_id=id, text=info_message)

    # 코로나 지원정책 이미지 답장
    elif (user_text == "피해지원정책"):
        bot.send_message(chat_id=id, text="최신 피해지원정책 가져오는 중...")
        covid_image_support_policy(image_num=10)
        # 이미지 한장만 보내기
        # bot.send_photo(chat_id=id, pho"to=open("./코로나이미지/0.png", 'rb'))
        # 이미지 여러장 묶어서 보내기
        photo_list = []
        for i in range(len(os.walk("./코로나지원정책").__next__()[2])): # 이미지 파일 개수만큼 for문 돌리기
            photo_list.append(telegram.InputMediaPhoto(open("./코로나지원정책/{}.png".format(i), "rb")))
        bot.sendMediaGroup(chat_id=id, media=photo_list)
        bot.sendMessage(chat_id=id, text=info_message)


echo_handler = MessageHandler(Filters.text, handler)
dispatcher.add_handler(echo_handler)