# -*- coding: utf-8 -*-
from redis import StrictRedis

redis = StrictRedis(host="192.168.0.111",
                    port=6380,
                    db=13,
                    decode_responses=True)

key_pattern_1 = "test_{}_first"
key_pattern_2 = "test_{}_second"

# for i in range(100):
#     redis.set(key_pattern_1.format(i), "test")
#     redis.set(key_pattern_2.format(i), "test")


def scan_keys(pattern: str) -> list:
    """
    扫描Redis库,获取某规则key列表
    :param pattern: key匹配规则
    :return: 某规则key列表
    """
    # 获取匹配某规则的所有key列表
    redis_keys_list = []

    scan_iter = redis.scan_iter(match=pattern)
    for keys in scan_iter:
        redis_keys_list.append(keys)

    return redis_keys_list


def get_zhongzhao_cache_key_list(patterns: list) -> list:
    """
    获取中招缓存key列表
    :param patterns: key规则
    :return: 中招缓存key列表
    :rtype: list
    """
    zhongzhao_cache_key_list = []
    for pattern in patterns:
        redis_keys_list = scan_keys(pattern=pattern)
        zhongzhao_cache_key_list.extend(redis_keys_list)

    return zhongzhao_cache_key_list


if __name__ == '__main__':
    patterns = ["test_*_first", "test_*_second"]
    key_list = get_zhongzhao_cache_key_list(patterns=patterns)
    print(len(key_list))
