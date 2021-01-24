# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from cubes.tutorial.sql import create_table_from_csv
from cubes import Workspace

engine = create_engine('sqlite:///data.sqlite')
create_table_from_csv(
    engine,
    "data.csv",
    table_name="irbd_balance",
    fields=[
        ("category", "string"),
        ("category_label", "string"),
        ("subcategory", "string"),
        ("subcategory_label", "string"),
        ("line_item", "string"),
        ("year", "integer"),
        ("amount", "integer")
    ],
    create_id=True
)

workspace = Workspace()
workspace.register_default_store("sql", url="sqlite:///data.sqlite")
workspace.import_model("model.json")
browser = workspace.browser("irbd_balance")
result = browser.aggregate()
print(result.summary["record_count"])  # 记录总数
print(result.summary["amount_sum"])  # 金额总计
result = browser.aggregate(drilldown=["year"])  # 下钻到年
for record in result:
    print(record)

result = browser.aggregate(drilldown=["item"])  # 下钻到item
for record in result:
    print(record)