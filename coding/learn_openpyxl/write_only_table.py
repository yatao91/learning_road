# -*- coding: utf-8 -*-
from openpyxl import Workbook

wb = Workbook(write_only=True)
ws = wb.create_sheet()

ws.append(["序号", "发布时间", "标题", "省份", "采购人", "中标单位", "中标金额", "代理机构"])
ws.append([1, "2020-01-01", "标题", "省份", "采购人", "中标单位", 100, "代理机构"])
ws.append([2, "2020-01-01", "标题", "省份", "采购人", "中标单位", 100, "代理机构"])
ws.append([3, "2020-01-01", "标题", "省份", "采购人", None, 100, "代理机构"])
ws.append([4, "2020-01-01", "标题", "省份", "采购人", "中标单位", 100, "代理机构"])
ws.append([5, "2020-01-01", "标题", "省份", "采购人", "中标单位", 100, "代理机构"])

wb.save("write_only_file.xlsx")
