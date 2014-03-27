#!/usr/bin/env python
# coding:utf-8
import sys
from fizzbuzz import fizz_buzz

if __name__ == '__main__':
    buf = raw_input('自然数を入力してください。\n-->',)
    
    if not buf.isdigit():
        print u'入力エラー'
        sys.exit()

    for i in range(int(buf)):
        print fizz_buzz(i)

