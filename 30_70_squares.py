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

header = 'SQUARES OF NUMBERS FROM 30 TO 70 TEST'
print header
print '-' * len(header)
print '\nPress Ctrl+C to stop\n'

while True:
  a = random.randint(30, 70)
  ans = raw_input('%d ^ 2 = ? ' % a)
  while not ans.isdigit():
    ans = raw_input('INVALID CHOICE !! %d ^ 2 = ? ' % a)
  ans = int(ans)
  cnt += 1
  if ans == a**2:
    print 'Correct !!'
    score += 1
  else:
    print 'Wrong !!'
    score -= 1
