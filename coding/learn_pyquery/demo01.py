# -*- coding: utf-8 -*-
from pyquery import PyQuery as pq

html = '''
<div id="container">
    <ul class="list">
         <li class="item-0">first item</li>
         <li class="item-1"><hardware href="https://ask.hellobi.com/link2.html">second item</hardware></li>
         <li class="item-0 active"><hardware href="https://ask.hellobi.com/link3.html"><span class="bold">third item</span></hardware></li>
         <li class="item-1 active"><hardware href="https://ask.hellobi.com/link4.html">fourth item</hardware></li>
         <li class="item-0"><hardware href="https://ask.hellobi.com/link5.html">fifth item</hardware></li>
     </ul>
 </div>
 '''

html_doc = pq(html)
print(html_doc('li'))
print(html_doc('#container .list li'))
print(type(html_doc('#container .list li')))
items = html_doc('.list')
print(type(items))
print(items)
lis = items.find('li')
print(type(lis))
print(lis)
lis = items.children()
print(type(lis))
print(lis)
lis = items.children('.active')
print(lis)

# web_doc = pq(url='http://www.baidu.com')
# print(web_doc('title'))
#
# file_doc = pq(filename='demo.html')
# print(file_doc('li'))
