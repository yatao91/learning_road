# -*- coding: utf-8 -*-
from pymongo import MongoClient

client = MongoClient(host="192.168.33.10", port=27017)

db = client.examples

resp = db.inventory.insert_one(
    {
        "item": "canvas",
        "qty": 100,
        "tags": ["cotton"],
        "size": {"h": 28, "w": 35.5, "uom": "cm"}
    }
)
print(dir(resp))
