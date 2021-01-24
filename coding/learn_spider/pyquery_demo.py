# -*- coding: utf-8 -*-
from pyquery import PyQuery as pq
import re


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


def extract_chinese_txt(html: str) -> str:
    """返回一个纯文本,并用逗号(,)对输入的html中的所有特殊字符替换"""
    pattern = "[\u4e00-\u9fa5]+"
    regex = re.compile(pattern)
    results = regex.findall(html)
    results = ",".join(results)
    return results


if __name__ == '__main__':
    raw_html = '''<p>年份：2019年早春</p><p>1、原料选自老班章茶区头春古树鲜叶。</p><p>2、 条索肥壮，梗叶相连，韧如蒲苇，犹如“橡筋”般的韧性和弹性，故名：橡筋茶。</p><p>3、入口强劲，彰显班章独特的霸气，生津快速，回甘无穷。</p><p>4、外盒中嵌入微型湿度调节系统，提供橡筋班章茶饼标准的陈化环境，利于其后期的转化。</p><p><img src="https://jm.bamatea.com/loadImage/editor/2019-08-27/be251f5f-f284-4b9f-9c83-b9bf327799b2.jpg" _src="https://jm.bamatea.com/loadImage/editor/2019-08-27/be251f5f-f284-4b9f-9c83-b9bf327799b2.jpg" style=""/></p><p><img src="https://jm.bamatea.com/loadImage/editor/2019-08-27/e44a105b-43ff-4b58-aa6a-4c8efc44a80a.jpg" _src="https://jm.bamatea.com/loadImage/editor/2019-08-27/e44a105b-43ff-4b58-aa6a-4c8efc44a80a.jpg" style=""/></p><p><img src="https://jm.bamatea.com/loadImage/editor/2019-08-27/689cc53d-edc5-4dfa-864c-18d0a5ecb2ee.jpg" _src="https://jm.bamatea.com/loadImage/editor/2019-08-27/689cc53d-edc5-4dfa-864c-18d0a5ecb2ee.jpg" style=""/></p><p><img src="https://jm.bamatea.com/loadImage/editor/2019-08-27/93adca13-ffcc-4298-9182-cb91f231e9a4.jpg" _src="https://jm.bamatea.com/loadImage/editor/2019-08-27/93adca13-ffcc-4298-9182-cb91f231e9a4.jpg" style=""/></p><p><br/></p>'''

    a, b, c, d = extract_text_from_html(raw_html)
    print(b)
