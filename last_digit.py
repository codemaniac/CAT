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

header = 'LAST DIGIT IN a^b TEST'
print header
print '-' * len(header)
print '\nPress Ctrl+C to stop\n'

while True:
  a = random.randint(2, 999)
  b = random.randint(10, 99999)
  ans = raw_input('last digit in %d^%d = ? ' % (a,b))
  while True:
    try:
      ans = int(ans)      
    except ValueError:
      ans = raw_input('INVALID CHOICE !! last digit in %d^%d = ? ' % (a,b))
      continue
    if ans not in range(10):
      ans = raw_input('INVALID CHOICE !! last digit in %d^%d = ? ' % (a,b))
      continue
    else:
      break     
  cnt += 1
  correct_ans = int((a**b) % 10)
  if ans == correct_ans:
    print 'Correct !!'
    score += 1
  else:
    print 'Wrong !!'
    score -= 1
