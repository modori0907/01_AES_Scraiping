import requests
from bs4 import BeautifulSoup
from genericpath import exists
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
import os
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import openpyxl



# ------- 変数一覧 ------- #
# 対象AES指定
AES = [
    {"AES_NO": 1, "host_name": "AES#1", "IP_ADDRESS": "aes1.aura8.avaya.tsuzuki.co.jp", "LOGINID": "cust", "PASSWORD": "Tdtcpw!7726"},
    {"AES_NO": 2, "host_name": "AES#2", "IP_ADDRESS": "aes1.aura8.avaya.tsuzuki.co.jp", "LOGINID": "cust", "PASSWORD": "Tdtcpw!7726"},
]

# ExcelのFile Name
File_Name = "sample.xlsx"
Sheet_name = "test_config"

# ---- 内部処理を行うため
# 対象AESを指定する
aes_i = 0
# excel記載処理で列を移動する処理
excel_i = 1


# ------- Excel ファイルを用意------- #
# 初期シート削除
wb = openpyxl.Workbook()
wb.remove(wb["Sheet"])
ws_new = wb.create_sheet(title=Sheet_name)

# ------- 各種処理 ------- #

# 証明書なくてもページを遷移させるために
capabilities = DesiredCapabilities.CHROME.copy()
capabilities['acceptInsecureCerts'] = True

# ウィンドウ表示処理の設定
options = Options()
# options.add_argument('--hide-scrollbars')
# options.add_argument('--incognito') # シークレットモード
# options.add_argument('--headless')


driver = webdriver.Chrome(executable_path='chromedriver.exe', desired_capabilities=capabilities, options=options)
driver.set_window_size(1080, 800)

# ------- ログイン処理に必要な関数定義 ------- #
#後でぐるぐる回せるようにする

IP_ADDRESS = AES[0]["IP_ADDRESS"]
LOGINID = AES[0]["LOGINID"]
PASSWORD = AES[0]["PASSWORD"]


driver.get(f"https://{IP_ADDRESS}/index.jsp")

# ページにアクセスする処理

Continue = driver.find_element_by_link_text('Continue To Login')
Continue.click()

login_id = driver.find_element_by_name("LoginForm:userName")
login_id.send_keys(LOGINID)

login_btn = driver.find_element_by_xpath('//*[@id="LoginForm:j_id34"]')
login_btn.click()

# input Passwd
passwd = driver.find_element_by_name("LoginForm:password")
passwd.send_keys(PASSWORD)
login_btn = driver.find_element_by_xpath('//*[@id="LoginForm:j_id36"]')
login_btn.click()

# 1 AES Services

LINK1 = "AE Services"

LINK1_click = driver.find_element_by_link_text(f'{LINK1}')
LINK1_click.click()

cur_url =driver.current_url  # 移動したURLの取得
# print(cur_url)
time.sleep(5)
html = driver.page_source.encode('utf-8')
soup = BeautifulSoup(html, 'lxml')
results = soup.find_all()

for result in results:
    print(result.text)


driver.close()
driver.quit()

# 参考
# https:/https://techacademy.jp/magazine/34387/techacademy.jp/magazine/34387
