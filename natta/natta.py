#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
import sys

import pandas as pd
from pandas.tools.plotting import scatter_matrix
import matplotlib.pyplot as plt

ref_info = ['first', 'second', 'third', 'forth', 'fifth', 'sixth']


class Natta:
    def __init__(self):
        self.data = pd.read_csv(
                '../_natta.csv', header=None, index_col=0, names=ref_info)
        pd.set_option('display.max_rows', 999)
        # self.frequency()
        # self.describe()
        # self.boxplot()
        # self.histogram()
        # self.realtionships_with_feature()
        # natta.compare_count_and_rank(7)
        self.test()

    def frequency(self):
        for i in range(len(ref_info)):  # 1 ~ 6 each
            print(self.data.groupby(ref_info[i]).count())

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
    sys.exit(0)
