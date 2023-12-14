#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import bit
import time

c = 0
Q1 = 346538096819291804893079641364924223074
Q2 = 1

start_time = time.time()
with open("python_result.txt", "a") as f1:
    for i in range(1, 100001):
        Q3 = Q1 - Q2
        Q1 = Q3
        c += 1
        f1.write(hex(Q3)[2:] + '\n')

        current_time = time.time()
        elapsed_time = current_time - start_time
        speed = c / elapsed_time
        print('\rCount:', c, '| Speed: {:.2f} /s'.format(speed), end='', flush=True)

print("\nThe job is done! Total time spent {} сек.".format(round(time.time() - start_time)))
input('Press Enter to exit the script > ')













