#!/usr/bin/env python3
import os
import getpass
import imglib
import db_interface
import loc_interface
import util
from multiprocessing import Lock, Value


def build_user_db(data, q, max_download):

  num, user, dpath, dname, sql, lock, reset, cursor, connection, loc, counter = data

  p_pict = imglib.ProcessPicture(data)

  offset_count = 0
  # print('build: ', num, ' done: ', done, ' offset_count: ', offset_count)
  if p_pict.m_reset:
    offset_count = p_pict.reset()
  else:
    offset_count, dirpath = p_pict.load_range(num)
    count = p_pict.spawn_thread(offset_count, dirpath)

  if num == 0:
    q.put(offset_count)
  else:
    q.put((num, dirpath, count))

def do_it(user, dpath, dname):

  p_list = []

  reset = True
  num = 0
  cursor = None
  connection = None
  max_download = None

  m = util.Manager()
  lock = m.RLock()
  sql = db_interface.SqlLite(dpath + dname)
  loc = loc_interface.GeoPy('user_agent = "zoby"')
#  loc = loc_interface.Default()
  q = util.Queue()
  counter = util.Counter(0)

  while True:

    data = (num, user, dpath, dname, sql, lock, reset, cursor, connection, loc, counter)
    p = util.Process(target = build_user_db, args = (data, q, max_download))
    p.start()

    if num == 0:
      p_num = q.get()
      cursor, connection = sql.open_db()
    else:
      p_list.append(p)

    reset = False
    if num == p_num or num > 120:
      print(num, ' == ', p_num)
      break
    num += 1

  for p in p_list:
    p.join()
    # print('process done: ', p.name)

  print('\ndo_it qsize: ', q.qsize())
  items = [q.get() for _ in range(q.qsize())]
  tot = 0
  for item in items:
    num, _, file_cnt = item
    # print(num, dirpath, file_cnt)
    tot += file_cnt

  print('tot files: ', tot)

  sql.close_db()

#####################################################################################
#                                   main
#####################################################################################

if __name__ == "__main__":

  start = util.print_start()

  dpath = os.getcwd() + '/'
  dname = 'rad-picture.db'
  user = getpass.getuser()

  do_it(user, dpath, dname)

  util.print_end(start)


