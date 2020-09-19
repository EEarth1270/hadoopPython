#!/usr/bin/env python
from operator import itemgetter
import sys

if __name__ == '__main__':
    for line in sys.stdin:
		a=line.split(',')
        if(a[4] == 39 && a[98] != ''):
            sys.stdout.write('{}\t1\n'.format(a[4]))