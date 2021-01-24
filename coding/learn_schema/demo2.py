# -*- coding: utf-8 -*-
from schema import Schema, And

chart_type = 'b'


def validate_chart_type(a):

    if chart_type not in ['hardware'] and a is True:
        return False
    else:
        return True


schema = Schema({"hardware": And(bool, validate_chart_type)})

data = {"hardware": True}

validated_data = schema.validate(data)

print(validated_data)
