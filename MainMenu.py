import attrs
from bs4 import BeautifulSoup
import lxml
import csv

# AESのメインメニューを取得（行間の空白行はあとで調整）
with open("aesmain.html", encoding="utf-8_sig") as file:  # utf-8_sigを記載することで
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")


# ------- 関数 ------- #


# データを値単位に変換する
# https://www.python.ambitious-engineer.com/archives/1843
def split_list(l, n):
    """
    リストをサブリストに分割する
    :param l: リスト
    :param n: サブリストの要素数
    :return:
    """
    for idx in range(0, len(l), n): # range(スタート、ストップ、ステップ)
        yield l[idx:idx + n] # ステップさせたい箇所までをスライス。l[0:5]など。




# テーブルを指定[x]で指定する。対象箇所
table = soup.find_all("table")[25]

# カラムを取得する処理
web_columns = table.findAll("th")
columns = []
for web_column in web_columns:
    columns.append(web_column.getText())

# 実データを取得する処理
web_datas = table.findAll("td")
datas = []
n = 0
for web_data in web_datas:
    datas.append(web_data.getText())
# print(datas)

# 指定した数でリストを分割する処理
datas_list = list(split_list(datas, 5))

print(datas_list)
# どこのテーブルを使えばよいのかを探す関数 #

"""
n = 0
for table in source_table:
    print(f"{n}::{table}")
    print("ここまでだよ------------------------------------------------------------")
    n += 1

"""


#
# n = 0
# for source in source_table[25]:
#
#     print(f"{n}     ☆/n{source}")
#     print("ここまで-------------------------")
#     n +=1

















# ★★検証★★

"""
all_anchor_tags = soup.find_all(name="a")
for tag in all_anchor_tags:
    # <a href = "/aesvcs/view/welcome/ctiWelcomeWarningPage.xhtml" > AEServices </a>
    print(tag.getText()) # 各アンカータグ(a)の中身だけ取得する。上の場合AEServices
    print(tag.get("href")) # 各アンカータグの内部に指定された値を取得する。上の場合、/aesvcs/view/welcome/ctiWelcomeWarningPage.xhtml
☆"""


"""
# <span style="font-size: 20px;font-weight:bold;">Application Enablement Services</span>
# ある値を特定するためのコード
# クラスを使う場合はclass_="sss"とする。

heading = soup.find(name="span", style="font-size: 20px;font-weight:bold;")
print(heading)
☆"""


# 取得データの指定
"""
<haed>
<link href="/aesvcs/a4j_3_1_4.GAcss/panel.xcss/DATB/eAH7-d11BQAH.wLe" rel="stylesheet" type="text/css"/>
</head>
"""

"""
#上の内容を取得するためのコード
# test_url = soup.select_one(selector="head link")
# print(test_url)

# idで指定する場合は#をつける
# name = soup.select_one(selector="#r1_side_bar")
# print(name)

# クラスで指定する場合は.をつける
# 複数ある場合はリストで取得が可能
headings = soup.select(".activeNavLink ")
print(headings)


#
# with open("aesmain.csv", "w", encoding='utf-8') as file:
#     writer = csv.writer(file)  #
#     for row in rows:
#         csvRow = []
#         for cell in row.findAll(['td', 'th']):
#             csvRow.append(cell.get_text())
#         writer.writerow(csvRow)
☆"""



