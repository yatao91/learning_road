# -*- coding: utf-8 -*-
import re

import requests
from openpyxl import Workbook
from pyquery import PyQuery as pq

num = 2


def extract_text_from_html(raw_html):
    """用pyquery提取raw_html的文本text"""
    if not raw_html:
        return None, raw_html, "", raw_html

    raw_html = raw_html.strip()

    if raw_html.startswith("</"):
        raw_html = "<" + raw_html[2:]
    # pyquery源码中有自动get URL的功能, 需要进行屏蔽(如果文档开头以http开始,则识别为URL)
    raw_html = "<br>" + raw_html
    try:
        pq_doc = pq(raw_html, parser="html")

        # 1.移除html 中 script 标签和style 标签, 这俩标签下的数据是跟正文无关的.
        script_items = pq_doc("script, style")
        for item in script_items.items():
            item.remove()
        # 2.移除html 标签中 value值是几万个英文和数字字符的value, 这些无意义的字符不能被es 分词 样例 201911148252764
        # 3.移除 src 是base64 长文本编码的情况,
        # 4.移除 href 是很长 url的情况
        # 这3种都是跟嗅探和标注无关的
        value_items = pq_doc("[value], [src], [href]")
        for item in value_items.items():
            item.remove_attr("value")
            item.remove_attr("src")
            item.remove_attr("href")
        text = pq_doc.text()
        result_raw_html = pq_doc.outer_html()
        if not text:
            return pq_doc, raw_html, "", result_raw_html
        return pq_doc, text, text, result_raw_html
    except Exception:
        return None, raw_html, "", raw_html


def extract_chinese_txt(html):
    """返回一个纯文本,并用逗号(,)对输入的html中的所有特殊字符替换"""
    pattern = "[\u4e00-\u9fa5]+"
    regex = re.compile(pattern)
    results = regex.findall(html)
    results = ",".join(results)
    return results


def write_data_to_excel(goods, sheet):
    global num

    for good in goods:
        sheet['A{}'.format(num)] = good['typeName']
        sheet['B{}'.format(num)] = good['subName']
        sheet['C{}'.format(num)] = good['goodsPrice']
        raw_desc = good['goodsDescription']
        _, html, _, _ = extract_text_from_html(raw_desc)
        sheet['D{}'.format(num)] = html

        num += 1


def start_spider(sheet):
    url = "https://jm.bamatea.com/Goods/GetGoodsByTypeIdAsync"

    data = {
        "typeId": "546a5fc2-071c-4553-9c79-78c3dc9f6f68"
    }

    while True:
        response = requests.post(url=url, json=data, headers={"Content-Type": "application/json"})
        response_dict = response.json()
        result = response_dict.get("result")
        model = result.get("model")
        goods_info_list = model.get("list_Goods_Dto")

        # 解析信息写入excel
        write_data_to_excel(goods=goods_info_list, sheet=sheet)

        # 组装下一页请求参数
        pageIndex = model.get("pageIndex") + 1
        print("爬取完成第{}页".format(pageIndex - 1))
        if pageIndex == 18:
            print("爬取完毕")
            break

        isDesc = model.get("isDesc")
        priceRange = model.get("priceRange")
        sortName = model.get("sortName")
        typeId = model.get("typeId")

        data = {
            "isDesc": isDesc,
            "pageIndex": pageIndex,
            "priceRange": priceRange,
            "sortName": sortName,
            "typeId": typeId
        }


if __name__ == '__main__':
    wb1 = Workbook()

    sheet1 = wb1.active

    sheet1.title = "茶叶信息"
    sheet1['A1'] = "类别"
    sheet1['B1'] = "名称"
    sheet1['C1'] = "原价"
    sheet1['D1'] = "简介"

    start_spider(sheet=sheet1)
    wb1.save("wangmeng.xlsx")
