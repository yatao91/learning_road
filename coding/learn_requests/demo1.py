# -*- coding: utf-8 -*-
import requests

resp = requests.get('http://epub.sipo.gov.cn/flzt.jsp')

print(resp.headers.get('Set-Cookie'))

resp2 = requests.get('http://epub.sipo.gov.cn/flzt.jsp', headers={
    "cookies": "cT6iSq1TseR480S=V7dkkX4e8CAEeEMT5KOMzoIcLdFEu146pieX5OS_FVuxCShMLum_Cu6cVXuGSsDz; Path=/; expires=Sun, 19 Aug 2029 08:41:06 GMT; HttpOnly, WEB=20111132; path=/"})

print(resp2.headers)
