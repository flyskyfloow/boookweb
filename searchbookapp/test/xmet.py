#!/usr/bin/env python
# -*- coding: utf-8 -*-
from lxml import etree
text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
'''
html = etree.HTML(text)
print(type(html))
# for i in html.xpath('//li'):
#     print(type(i))

# for i in html.xpath('//li/@class'):
#     print(i)

# for i in html.xpath('//li/a[@href="link1.html"]'):
#     print(i)

# xpath / 是用来获取子元素， // 获取不是子元素
print(html.xpath('//li/a'))