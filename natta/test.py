#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
import sys

from natta import Natta

class Test(Natta):
    def __init__(self):
        Natta.__init__(self)
        
        
    def check_all(self):
        for i in range(100, self.total):
            print(self.data.get_value(i, 'first'))
                        

if __name__ == '__main__':
    test = Test()

    test.check_all()

    sys.exit(0)
