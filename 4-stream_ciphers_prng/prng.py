#!/usr/bin/env python
from __future__ import division

"""
Thi is very basic LCG function.

Xi+1 = (aXi + c) mod M ve i=0,1,2,3
Ri= Xi/M

You are free to select random values for xZero, a, c and Mod variables.
xZero is our initialization vector.
"""


class LCG(object):
    def __init__(self, iv):
        self.xZero = iv

    def generate(self):
        a = 7**7  # Value is = 823543
        c = 5**10  # Value is = 9765625
        mod = 2**24
        self.xZero = (a * self.xZero + c) % mod
        return self.xZero / mod

feed = LCG(1826618237451)  # Random Number

for i in range(10):
    print feed.generate()
