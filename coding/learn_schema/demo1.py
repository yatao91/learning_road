# -*- coding: utf-8 -*-
from schema import Schema, And, Use, Optional

config_schema = Schema(
    {
        "chart_name": str,
        "chart_type": str,
        "chart_info": str,
        "view_id": int,
        "chart_config": {
            "x_axis": {
                "first_x": {
                    "field_key": str,
                    "field_type": str,
                    "options": {
                        "order": str,
                        "size": int,
                        "label_name": str,
                        "num_interval": int,
                        "time_interval": str,
                        "max_top": int,
                        "min_top": int
                    }
                },
                Optional("second_x"): {
                    "field_key": str,
                    "field_type": str,
                    "options": {
                        "order": str,
                        "size": int,
                        "label_name": str,
                        "num_interval": int,
                        "time_interval": str,
                        "max_top": int,
                        "min_top": int
                    }
                },
                Optional("third_x"): {
                    "field_key": str,
                    "field_type": str,
                    "options": {
                        "order": str,
                        "size": int,
                        "label_name": str,
                        "num_interval": int,
                        "time_interval": str,
                        "max_top": int,
                        "min_top": int
                    }
                }
            },
            Optional("y_axis"): {
                "field_key": str,
                "agg_type": str
            },
            Optional("time_condition"): {
                "field_key": str,
                "gte": str,
                "lte": str
            },
            Optional("advance"): {
                "is_mom": bool,
                "is_yoy": bool,
                "has_other": bool
            }
        }
    }
)

data = {
    "chart_name": "测试",
    "chart_type": "直方图",
    "chart_info": "这是一个测试图表",
    "view_id": 1,
    "chart_config": {
        "x_axis": {
            "first_x": {
                "field_key": "province",
                "field_type": "keyword",
                "options": {
                    "order": "desc",
                    "size": 10,
                    "label_name": "省份",
                    "num_interval": 0,
                    "time_interval": "",
                    "max_top": 0,
                    "min_top": 0
                }
            }
        },
        "time_condition": {
            "field_key": "publish_time",
            "gte": "2018-01-01",
            "lte": "2018-07-31"
        },
        "advance": {
            "is_mom": False,
            "is_yoy": False,
            "has_other": False,
        }
    }
}

validated_data = config_schema.validate(data)

class chart_schema(Schema):

    __i

    super(s)

print(validated_data)
