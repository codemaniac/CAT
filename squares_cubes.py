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

header = 'SQUARE-CUBE TEST'
print header
print '-' * len(header)

print '\nPress Ctrl+C to stop\n'

while True:
  x = random.randint(2, 25)
  p = random.choice([2,3])
  p_word = 'squared' if p == 2 else 'cubed'  
  ans = raw_input('%d %s = ? ' % (x,p_word))
  while not ans.isdigit():
    ans = raw_input('INVALID CHOICE !! %d %s = ? ' % (x,p_word))
  ans = int(ans)
  cnt += 1
  if ans == x**p:
    print 'Correct !!'
    score += 1
  else:
    print 'Wrong !!'
    score -= 1
