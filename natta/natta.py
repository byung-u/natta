#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
import sys
import random

import pandas as pd
from pandas.tools.plotting import scatter_matrix
import matplotlib.pyplot as plt

MAX_SORT_RANGE = 4
ref_info = ['first', 'second', 'third', 'forth', 'fifth', 'sixth']


def get_random_value(natta_submit, result):
    if len(result) == 1:
        natta_submit.append(result[0])
        return 0

    random.shuffle(result)
    if (result[0] in natta_submit):
        return -1
    else:
        natta_submit.append(result[0])
        return 0


class Natta:
    def __init__(self, flag=1):
        self.data = pd.read_csv(
                '../_natta.csv', header=None, index_col=0, names=ref_info)
        self.total = len(self.data.index)

        self.this_week_num = []
        for i in range(6):
            self.this_week_num.append(
                    self.data.get_value(self.total, ref_info[i]))

        if flag == 1:
            print('this: ', self.this_week_num, '\n\n')

    def check_by_past_week(self, lucky_num=None):
        # print(self.data.columns)
        # print(len(self.data.index))
        # print(self.data.eval)
        # print(self.data.get_value(1, ref_info[0]))

        if (lucky_num is None or len(lucky_num) == 0):
            lucky_num = self.this_week_num

        last_max = {}
        natta_submit = []
        for i in range(len(ref_info)):  # 1 ~ 6 each
            last_max.clear()
            for j in range(2, self.total):
                past_week_num = self.data.get_value(j, ref_info[i])
                if (past_week_num == lucky_num[i]):
                    last_week_num = self.data.get_value(j-1, ref_info[i])
                    cnt = last_max.get(last_week_num)
                    if cnt is None:
                        cnt = 0
                    last_max[last_week_num] = cnt + 1
            sort_result = sorted(
                    last_max.items(), key=lambda x: x[1], reverse=True)

            result = []
            max_range = len(sort_result)
            if max_range > MAX_SORT_RANGE:
                max_range = MAX_SORT_RANGE

            for j in range(max_range):
                result.append(sort_result[j][0])

            while True:
                ret = get_random_value(natta_submit, result)
                if (ret == 0):
                    break
        return natta_submit

    def check_by_next_week(self, lucky_num=None):
        if (lucky_num is None or len(lucky_num) == 0):
            lucky_num = self.this_week_num


        next_max = {}
        natta_submit = []
        for i in range(len(ref_info)):  # 1 ~ 6 each
            next_max.clear()
            for j in range(1, self.total-1):
                past_week_num = self.data.get_value(j, ref_info[i])
                if (past_week_num == lucky_num[i]):
                    next_week_num = self.data.get_value(j+1, ref_info[i])
                    cnt = next_max.get(next_week_num)
                    if cnt is None:
                        cnt = 0
                    next_max[next_week_num] = cnt + 1
            sort_result = sorted(
                    next_max.items(), key=lambda x: x[1], reverse=True)
            # print([i], sort_result[-3:])
            result = []
            max_range = len(sort_result)
            if max_range > MAX_SORT_RANGE:
                max_range = MAX_SORT_RANGE

            for j in range(max_range):
                result.append(sort_result[j][0])

            while True:
                ret = get_random_value(natta_submit, result)
                if (ret == 0):
                    break
        return natta_submit

    # Below functions are just pasdas test.
    def frequency(self, idx=None):
        if idx is None:
            for i in range(len(ref_info)):  # 1 ~ 6 each
                print(self.data.groupby(ref_info[i]).count())
        else:
            print(self.data.groupby(ref_info[idx-1]).count())

    def describe(self):
        ''' mean : 평균
            std  : 표준편차 '''
        print(self.data.describe())

    def boxplot(self):
        self.data.boxplot()
        plt.show()

    def histogram(self):
        self.data.hist()
        plt.show()
        '''
        TODO : Do not use yet, check it first.

        for i in range(len(ref_info)):
            print(self.data.groupby(ref_info[i]).hist())
            plt.show()
            return
        '''

    def realtionships_with_feature(self):
        # 상호간의 관계도
        scatter_matrix(self.data, alpha=0.2, figsize=(6, 6), diagonal='kde')
        plt.show()

    def compare_count_and_rank(self, i=0):

        if (i > len(ref_info)):  # limit
            i = 6

        if (i != 0):
            i = i-1  # for buffer index

        d1 = self.data.groupby(ref_info[i]).count()
        d2 = self.data.groupby(ref_info[i]).count().rank(method='first')
        # http://pandas.pydata.org/pandas-docs/version/0.18.1/merging.html
        df = pd.concat([d1, d2], axis=1)
        # df = df.reset_index(drop=True) # useless
        print(df)

    def test(self):
        print(self.data.info())
        # 공분산(covariance)
        # print(self.data.cov())
        # 상관분석(correlations)
        # print(self.data.corr())
        # print(self.data.groupby(ref_info[0]).count().rank(method='first'))
        # for i in range(len(ref_info)): # 1 ~ 6 each
        # print(self.data.groupby(ref_info[i]).count())
        # print(self.data.groupby(ref_info[i]).count().rank(method='first'))
        # print(self.data.rank(method='first'))


if __name__ == '__main__':
    natta = Natta()

    print('by past :', natta.check_by_past_week())
    print('by next :', natta.check_by_next_week())
    # natta.frequency(1)
    # self.frequency()
    # self.describe()
    # self.boxplot()
    # self.histogram()
    # self.realtionships_with_feature()
    # natta.compare_count_and_rank(7)
    # self.test()
    sys.exit(0)
