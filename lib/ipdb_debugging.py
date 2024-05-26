#!/usr/bin/env python3

import ipdb

def plus_two(num):
    result=num + 2
    ipdb.set_trace()
    return result
num=3
result = plus_two(num)
print(result)