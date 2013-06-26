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

header = 'TABLES TEST'
print header
print '-' * len(header)

print '\nPress Ctrl+C to stop\n'

while True:
  x = random.randint(2, 20)
  y = random.randint(2, 20)  
  ans = raw_input('%d X %d = ? ' % (x,y))
  while not ans.isdigit():
    ans = raw_input('INVALID CHOICE !!\n%d X %d = ? ' % (x,y))
  ans = int(ans)
  cnt += 1
  if ans == x*y:
    print 'Correct !!'
    score += 1
  else:
    print 'Wrong !!'
    score -= 1
