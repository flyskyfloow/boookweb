#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests

URL = "https://hq.ssrn.com/rankings/loginAjax.cfm?login=true&username=2373808611@qq.com&pass=" \
      "502302555&forwardURL=https%3A%2F%2Fhq%2Essrn%2Ecom%2Frankings%2FRanking%5Fdisplay%2Ecfm%3FTRN%5FgID%3D10"
s = requests.Session()
s.get(URL)
r = s.get("https://hq.ssrn.com/rankings/Ranking_display.cfm?TRN_gID=10").text
print(r.text)
