# -*- coding: utf-8 -*-
# !/usr/bin/env python
# vim: set fileencoding=utf-8 :

"""
#
# Author:   Noname
# URL:      https://github.com/pettan0818
# License:  MIT License
# Created:  2015-05-18
#

# Usage
#
"""
import pandas


def merge_category_dummy(original):
    """
    pandasのダミー変数作成関数により、
    ダミー変数を辞書データにくっつける
    """
    dummy_data = pandas.get_dummies(original['eval'])

    merged_df = pandas.concat([original['word'], dummy_data], axis=1)

    return merged_df


if __name__ == '__main__':
    PN_DIC_NAME = "opinion_dict.csv"

    DIC_PN = pandas.read_csv(PN_DIC_NAME, sep='\t', header=None)

    DIC_PN.columns = ['word', 'eval', 'usecase']

    DIC_WITH_DUMMY = merge_category_dummy(DIC_PN)

    print DIC_WITH_DUMMY
