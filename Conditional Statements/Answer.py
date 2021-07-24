#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input().strip())
    if N%2 != 0 or ((N > 5 and N < 21) and N%2 == 0):
        print("Weird")
    else:
        print("Not Weird")
