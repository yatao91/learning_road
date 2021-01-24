# -*- coding: utf-8 -*-


def mattrgetter(*attrs):
    """
    获取某对象的多个属性,不存在时返回None
    :param attrs: 各属性值,str
    :return: function
    """
    return lambda obj: {attr: getattr(obj, attr, None) for attr in attrs}


if __name__ == '__main__':
    func = mattrgetter("hardware", "b")
    obj = []
    data = func(obj)
    print(data)
