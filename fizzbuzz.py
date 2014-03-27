#!/usr/bin/env python
# coding:utf-8

def fizz_buzz(buf):
    if not buf.isdigit():
        return buf

    number = int(buf)

    if number % 15 is 0:
        return "FizzBuzz"
    elif number % 3 is 0:
        return "Fizz"
    elif number % 5 is 0:
        return "Buzz"
    else:
        return buf

