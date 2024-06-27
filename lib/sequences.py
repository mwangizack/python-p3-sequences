#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        print([])
    elif length == 1:
        print([0])
    elif length == 2:
        print([0,1])
    else:
        fib = [0,1]
        count = 2
        while count < length:
            next_element = fib[-1] + fib[-2]
            fib.append(next_element)
            count += 1
        print(fib)
 