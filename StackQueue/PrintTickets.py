# -*- coding:utf-8 -*-
"""
bj->sh sh->hz hz->fz fz->nc nc->cs

"""


def printTickets(data):
    reverseData = {}
    for k, v in data.items():
        reverseData[v] = k
    start = None
    for k, v in data.items():
        if k not in reverseData.keys():
            start = k
            break
    to = data[start]
    while to is not None:
        print(" " + start + "-->" + to + " ")
        start = to
        to = data[to]


data = {"bj": "sh", "sh": "hz", "hz":"fz"}
printTickets(data)