#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import signal
import sys

cnt = 0
score = 0

def signal_handler(signal, frame):
  print '\n' + '-'*80
  print 'score = %d/%d' % (score, cnt)
  print 'Bye !'
  sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

header = 'DIVISIBILITY TEST'
print header
print '-' * len(header)
print '\nPress Ctrl+C to stop\n'

n = int(raw_input("Enter divisibility test number: "))

while True:
  x = random.randint(1, 99999)
  ans = raw_input("%d divisible by %d ? (y/n): " % (x, n)).lower()
  while ans not in ['y','n']:
    ans = raw_input("INVALID CHOICE !! %d divisible by %d ? (y/n): " % (x, n)).lower()
  cnt += 1
  if (x % n == 0):
    if ans == 'y':
      score += 1
      print 'Correct !!'
    elif ans == 'n':
      score -= 1
      print 'Wrong !!'
  else:
    if ans == 'y':
      score -= 1
      print 'Wrong !!'
    elif ans == 'n':
      score += 1
      print 'Correct !!'
