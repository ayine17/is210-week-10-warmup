#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""week 10, Task 07"""


DATA = {
    2: 7493945,
    76: 4654320,
    3: 4091979,
    90: 1824881,
    82: 714422,
    45: 1137701,
    10: 374362,
    0: 326226,
    -15: 417203,
    -56: 333525,
    67: 323451,
    99: 321696,
    21: 336753,
    -100: 361237,
    55: 1209714,
    5150: 1771800,
    42: 4714011,
    888: 14817667,
    3500: 13760234,
    712: 10903322,
    7: 10443792,
    842: 11716264,
    18584: 10559923,
    666: 9275602,
    70: 11901200,
    153: 12074784,
    8: 4337229
}


def iter_dict_funky_sum(data):
    """a function to calcuate the runing total of value minus the key

    Args:
        DATA(dict): a set of key/value pairs of intergers
    return: Return integer sum of the funky total of value minus the key

    example:

        >> import task_07
        >>> task_07.iter_dict_funky_sum(task_07.DATA)
        140166242
    """

    running_total = 0
    for key, value in data.iteritems():
        running_total += (value - key)
    return running_total
