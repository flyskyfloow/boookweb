#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pickle
import time
from selenium import webdriver
urllist = ("https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2900447","https://papers.ssrn.com/sol3/papers.cfm?abstract_id=962461")
# def loginDownload():
driver = webdriver.Chrome()
driver.get('https://hq.ssrn.com/login/pubsigninjoin.cfm')
elemname = driver.find_element_by_name("input-email")
elekey = driver.find_element_by_name('input-pass')
elemname.send_keys("2373808611@qq.com")
elekey.send_keys("guo502302")
driver.find_element_by_id('signinBtn').click()
driver.back()
# driver.get('https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1968579')
# driver.find_element_by_id('downloadPdf').click()
# driver.find_element_by_xpath("(//a[contains(text(),'Download this Paper')])[2]").click()


def download(url):
    driver.get(url)
    driver.find_element_by_id('downloadPdf').click()
    time.sleep(3)


if __name__ == "__main__":
    for i in urllist:
        download(i)






