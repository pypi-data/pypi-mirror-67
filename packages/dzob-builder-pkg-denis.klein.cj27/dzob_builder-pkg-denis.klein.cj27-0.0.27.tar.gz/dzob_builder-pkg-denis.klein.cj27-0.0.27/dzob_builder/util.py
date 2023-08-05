from multiprocessing import Process, Lock, Queue, Manager, Value
from datetime import datetime as dt
import time
import threading

##########################################################################################################
#
#                             Util
#
##########################################################################################################

class Counter(object):

  def __init__(self, initval=0):
    self.val = Value('i', initval)
    self.lock = Lock()

  def increment(self):
    with self.lock:
      self.val.value += 1

  def value(self):
    with self.lock:
      return self.val.value

def get_time():
  return time.time()

def get_time_now():
  return dt.now()

def print_elapse(title, stime):

  etime = dt.now()
  elapse = etime - stime

  hrs = int(elapse.seconds / (60 * 60))
  mn = int((elapse.seconds - hrs * 60 * 60) / (60))
  sec = int(elapse.seconds - (hrs * 60 * 60) - (mn * 60))

  # print(title, ' done in %02d:%02d:%02d' %(hrs, mn, sec))
  txt = ' done in ...{:02}:{:02}:{:02}'.format(hrs, mn, sec)

  return title + txt, etime

def prt_time(s_time):

  txt_time = str(s_time)
  pos = txt_time.find('.')

  if pos == -1:
    return txt_time

  return txt_time[:pos]

def print_start():

  ts_now = get_time()
  st_start = dt.fromtimestamp(ts_now).strftime('%Y-%m-%d %H:%M:%S')
  print('\n\nstarting building at.... {0}'.format(st_start))

  return dt.now()

def print_end(st):

  txt, _ = print_elapse('', st)
  print('\n\n{0}, done...\n\n'.format(txt))
