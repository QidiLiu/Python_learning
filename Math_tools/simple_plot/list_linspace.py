# /usr/bin/env python3
# -*- coding: utf-8 -*-

'input: start, stop, sum;\noutput: a linspace list'

def list_linspace(start, stop, sum):
    output_list = [start]
    for i in range(sum-1):
        output_list.append(output_list[-1] + (stop-start)/sum)
    return output_list

if __name__ == "__main__":
    pass