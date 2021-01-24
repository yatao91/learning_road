from schema import Schema, And


class ChartSchema(Schema):

    def __init__(self, chart_type, schema, error=None, ignore_extra_keys=False):
        self.chart_type = chart_type
        super().__init__(schema=schema, error=error, ignore_extra_keys=ignore_extra_keys)
        self.__class__ = Schema


from re import match


def is_phone_num(phone):
    """
    校验是否是合法手机号码
    :param phone: 要校验的合法手机号码
    :type phone: str
    :return: 是否是合法手机号码
    :rtype: bool
    """
    if match("^[0-9]{11}$", phone):
        return True
    return False


test_chart_schema = ChartSchema(chart_type="line_chart", schema={"phone": And(str, is_phone_num)})

# test_schema = Schema({"phone": And(str, is_phone_num)})
#
# params = test_schema.validate({"phone": "15754311232"})
#
# print(params)

params_chart = test_chart_schema.validate(data={"phone": "15754311232"})

print(params_chart)
