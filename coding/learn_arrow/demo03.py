import arrow


def make_time_suffix(time_condition: dict) -> str:
    """
    组装企业详情页时间过滤后缀用作组成缓存field
    :param time_condition: 时间过滤条件
    :return:
    """
    time_condition_gte_int = time_condition.get("time_condition_gte")
    time_condition_lte_int = time_condition.get("time_condition_lte")
    time_condition_lte_int -= 1
    time_gte_arrow = arrow.get(time_condition_gte_int / 1000).to(tz="Asia/Shanghai")
    time_lte_arrow = arrow.get(time_condition_lte_int / 1000).to(tz="Asia/Shanghai")
    gte_year_str = time_gte_arrow.strftime("%Y")
    lte_year_str = time_lte_arrow.strftime("%Y")
    time_suffix_str = gte_year_str + lte_year_str

    return time_suffix_str


if __name__ == '__main__':
    time_condition = {"time_condition_gte": 1514736000000,
                      "time_condition_lte": 1577808000000}
    time_suffix_str = make_time_suffix(time_condition)
    print(time_suffix_str)
