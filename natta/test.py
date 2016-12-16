#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
import sys

from natta import Natta
from natta import ref_info

MAX_NUM_RANGE = 6


class Test(Natta):
    def __init__(self):
        Natta.__init__(self)

    def check_all(self, start=100):
        lucky_num = []
        result_cnt = 0
        for i in range(start, self.total):
            lucky_num[:] = []
            for j in range(MAX_NUM_RANGE):
                lucky_num.append(self.data.get_value(i, ref_info[j]))

            by_past = self.check_by_past_week(lucky_num)
            ret = self.compare_lucky_with_nattaresult(lucky_num, by_past)
            if ret > 2:
                print([i], 'past matched: ', ret, lucky_num, by_past)
                result_cnt += 1

            by_next = self.check_by_next_week(lucky_num)
            ret = self.compare_lucky_with_nattaresult(lucky_num, by_next)
            if ret > 2:
                print([i], 'next matched: ', ret, lucky_num, by_next)
                result_cnt += 1

        if result_cnt == 0:
            result_msg = 'Result: 0/%d 0%%' % (self.total - start)
        else:
            result_msg = 'Result: %d/%d %d%%' % (
                    result_cnt, self.total - start,
                    result_cnt * 100 / (self.total - start))
        print(result_msg)

    def compare_lucky_with_nattaresult(self, lucky_num, compare_num):
        cnt = 0
        for i in range(MAX_NUM_RANGE):
            if (lucky_num[i] in compare_num):
                cnt += 1
        return cnt

if __name__ == '__main__':
    test = Test()

    if len(sys.argv) > 1:
        if str.isdecimal(sys.argv[1]):
            input_num = int(sys.argv[1])
            if input_num < 100 or input_num > test.total:
                print('Use default 730, range:100 < input < ', test.total)
                input_num = 730
        else:
            print('Use default 730, input value is not decimal')
            input_num = 730

        test.check_all(input_num)
    else:
        test.check_all()
    sys.exit(0)
