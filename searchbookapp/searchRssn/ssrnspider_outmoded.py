#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import re
import logging
from bs4 import BeautifulSoup
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"
logging.basicConfig(
    filename='ssrn.log',
    level=logging.ERROR,
    format=LOG_FORMAT,
    datefmt=DATE_FORMAT
)


def str2num(s):
    return re.sub("[\s,]", "", s)


def str2int(s):
    return int(str2num(s))


def str2float(s):
    return float(str2num(s))


class Ssrn(object):
    def __init__(self):
        self.host = "guo"
        self.sex = "man"
        print(self.host)

#   获取 paper 信息
    @staticmethod
    def getPaperInfoList():
        doublesqllist = []
        listpage = []
        URL = "https://hq.ssrn.com/rankings/loginAjax.cfm?login=true&username=2373808611@qq.com&pass=" \
      "502302555&forwardURL=https%3A%2F%2Fhq%2Essrn%2Ecom%2Frankings%2FRanking%5Fdisplay%2Ecfm%3FTRN%5FgID%3D10"
        s = requests.Session()
        # 获取登录cookie值 后续访问继续使用当前cookie 值
        s.get(URL)
        # 访问页面
        urlstart = "https://hq.ssrn.com/rankings/Ranking_display.cfm?npage="
        urlend = "&RequestTimeout=5000&TMY_gID=2&TRN_gID=10&runid=70198"
        for m in range(1, 2):
            listpage.append(urlstart + str(m) + urlend)
        for page in listpage:
            content = s.get(page).text
            soup = BeautifulSoup(content, "lxml")
            print(page)
            # print(soup)
            # print("开始过滤")
            # print(type(soup))
            # 获取论文列表(tr class 属性 TableRowDark and TableRowLight)
            lists = soup.body.find_all("tr", {"class": "TableRowDark"}) + \
                    soup.body.find_all("tr", {"class": "TableRowLight"})
            # print(type(lists))
            for i in lists:
                sqllist = []
                # a1 是个集合 a1[1] 是tag
                a1 = i.findAll("td")
                # a2 是一个 含有a标签的集合
                a2 = a1[1].findAll("a")
                title = a2[0].get_text()
                link = a2[0]["href"]
                author = a2[1].getText()
                gid = int(re.split("=", link)[-1])
                downloads = str2int(a1[3].getText())
                sqllist.append(gid)
                sqllist.append(str(title))
                sqllist.append(str(author))
                sqllist.append(str(link))
                sqllist.append(downloads)
                doublesqllist.append(sqllist)
        return doublesqllist

if __name__ == "__main__":
    mm = Ssrn()
    tt = mm.getPaperInfoList()
    print(len(tt))




