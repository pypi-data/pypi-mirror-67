#!/usr/bin/env python3

import os
import db_interface
import json
import util

# h_path = '/home/denis/Pictures/'

dic_state = ['not-done', 'in-progress', 'complete']

##########################################################################################################
#
#
##########################################################################################################

class ProcessPicture(object):

  def __init__(self, data, max_download = None):

    pnum, user, dpath, db_name, sql, lock, reset, cursor, connection, loc, counter = data

    self.m_fno = 0
    self.m_dir_dic = {}
    self.m_cursor = cursor
    self.m_connection = connection
    self.m_pnum = pnum
    self.m_pic_path = '/home/' + user + '/Pictures'
    self.m_dest_path = dpath
    self.m_db_name = db_name
    self.m_db_interface = sql
    self.m_loc_interface = loc
    self.m_lock = lock
    self.m_reset = reset
    self.m_counter = counter
    self.m_max_download = max_download
    self.m_s_time = util.get_time_now()

  def format_date(self, date):

    if date is 'Unknown':
      return date
    pos = date.find(' ')
    assert pos != -1
    date = date.replace(':', '-', 2)
    return date

  def clean_input(self, strg):

    strg = strg.replace('\'', '_')
    strg = '\'' + strg + '\''

    return strg

  def clean_dir(self, ext):

    for dirpath, _, filenames in os.walk(self.m_pic_path):

      fpath = dirpath
      fpath = fpath.replace('.', '') + '/'
      for filename in filenames:
  #      print(basepath + fpath)
        if filename.lower().find(ext.lower()) != -1:
          # print(fpath + filename)
          try:
            os.remove(fpath + filename)
          except Exception as e:
            print('error: {0}'.format(e))

  def reset(self):

    self.clean_dir('-resize.JPG')
    self.clean_dir('-thumb.JPG')
    self.build_json_dic()
    self.save_json_dic()

    try:
      os.remove(self.m_db_name)
    except Exception:
      pass

    self.m_cursor, self.m_connection = self.m_db_interface.open_db()
    self.create_table('PICTURE')
    print('reset done len: {0} {1}'.format(len(self.m_dir_dic), self.m_pic_path))
    self.m_db_interface.close_db()

    return len(self.m_dir_dic)

  def create_table(self, table):

    sql_stmt = "DROP TABLE IF EXISTS %s" % table
    self.m_db_interface.execute(sql_stmt)

    sql_stmt = "CREATE TABLE %s (ImageNo integer PRIMARY KEY, %s, %s, %s, %s, %s, %s, %s)" \
      % (table, 'FileName',  'UrlOrg', 'UrlResize', 'UrlThumb', 'Date', 'Orientation', 'Location')
    self.m_db_interface.execute_commit(sql_stmt)

  def read_json(self):

    if os.path.isfile(self.m_dest_path + 'json_dir.json'):
      with open(self.m_dest_path + 'json_dir.json') as json_file:
        self.m_dir_dic = json.load(json_file)

  def save_json_dic(self):

    jfile = json.dumps(self.m_dir_dic)
    f = open('./json_dir.json', 'w')
    f.write(jfile)
    f.close()

  def build_json_dic(self):

    exclude_dir = []
    self.m_dir_dic = {}

    # print('build_json_dic: ', self.m_pic_path)
    for dirpath, _, filenames in os.walk(self.m_pic_path):
      if any(ext in dirpath for ext in exclude_dir):
        continue

      fpath = dirpath
      fpath = fpath.replace('.', '') + '/'
      dirpath += '/'
      file_no = 0
      for filename in filenames:
        _, ext = os.path.splitext(fpath + filename)
        if ext.lower() == '.jpg' or ext.lower() == '.jpeg':
          file_no += 1

      if file_no != 0:
        # print('fpath {0} {1}'.format(file_no, fpath))
        assert self.m_dir_dic.get(fpath) == None
        self.m_dir_dic.update({fpath : (file_no, dic_state[0])})

    print('build_json_dic len: {0} {1}'.format(len(self.m_dir_dic), self.m_pic_path))

  def load_range(self, num):

    offset_count = 0
    assert num == self.m_pnum
    file_cnt = 0
    with self.m_lock:
      # print('read_json acquire: ', self.m_pnum)
      self.read_json()

      for dirpath, tup in sorted(self.m_dir_dic.items()):

        dcount, flag = tup
        # print('\n{0} is -> {1}'.format(dirpath, flag))
        if flag == dic_state[2]:
          # print('{0} is {1} {2}'.format(dirpath, flag, offset_count))
          offset_count += dcount
          continue
        if flag == dic_state[1]:
          # print('{0} is {1} {2}'.format(dirpath, flag, offset_count))
          offset_count += dcount
          continue

        assert flag == dic_state[0]
        self.m_dir_dic[dirpath] = [dcount, dic_state[1]]
        self.save_json_dic()
#        self.spawn_thread(offset_count, dirpath)
        file_cnt += dcount
        break
        # print(self.m_pnum, dirpath, ' state: ', self.m_dir_dic[dirpath])

    # print(self.m_pnum, done, offset_count)
    return offset_count, dirpath

  def spawn_thread(self, offset_count, dict_path):

    dcount, _ = self.m_dir_dic[dict_path]
    max_download = 10
    max_len = dcount
    thread_list = []

    if max_download > max_len:
      max_download = max_len

    count = 0
    idx   = 0

    geolocator = self.m_loc_interface.get_geopy()
   #  print('\np_num: ', self.m_pnum, ' with: ', dcount, dict_path)
    q = util.Queue()
    while count < max_len:

      start_index = idx * max_download
      end_index   = start_index + max_download

      if end_index >= max_len:
        end_index = max_len

      # print('spawn_thread start_index: ', start_index, ' end_index: ', end_index)
      thread = util.threading.Thread(target = self.get_thread_range, args = (q, dict_path, offset_count, start_index, end_index, geolocator))
      thread.start()
      thread_list.append((thread, end_index - start_index))

      count += max_download
      idx += 1

    for thread, count in thread_list:
      thread.join()
      # print('thread: ', count)

    # print('spawn_thread: ', len(thread_list))
    items = [q.get() for _ in range(q.qsize())]
    for sql_stmt in items:
      self.m_db_interface.execute(sql_stmt)

    try:
      self.m_db_interface.commit()
      # print('commited ', file_no)
    except Exception as e:
      print('Exception: ',  e, self.m_pnum, dict_path)

    # print('spawn_thread: ', len(items))
    return dcount

  def get_thread_range(self, q, dict_path, offset_count, s_idx, e_idx, geolocator):

    filenames = os.listdir(dict_path)
    # print('get_thread_range offset_count: ', offset_count, ' s_idx: ', s_idx, ' e_idx: ', e_idx)

    for idx in range(s_idx, e_idx):
      name = filenames[idx]
      filename = dict_path + name
      _, ext = os.path.splitext(filename)
      if not (ext.lower() == '.jpg' or ext.lower() == '.jpeg'):
        # print(' process: {0} {1} {2}'.format(self.m_pnum, filename, ext))
        continue

      # print('get_thread_range p_num: ', self.m_pnum, ' idx: ', idx, filename)
      date, location, orientation, rz_name, th_name = self.m_loc_interface.get_picture_data(filename, geolocator)
      date = self.format_date(date)
      pos = filename.find(self.m_pic_path)
      assert pos != -1
      filename = filename[pos + len(self.m_pic_path):]

      try:

        with self.m_lock:

          # print('name: {0}\nfilename: {1}\nrz_name: {2}\nth_name: {3}'.format(name, filename, rz_name, th_name))
          sql_stmt = 'INSERT INTO PICTURE (ImageNo, Date, Location, Orientation, FileName, UrlOrg, UrlResize, UrlThumb) \
          VALUES (%s, %s, %s, %s, %s, %s, %s, %s);' \
            % (self.m_counter.value(), self.clean_input(date), self.clean_input(str(location)), self.clean_input(str(orientation)),
            self.clean_input(name), self.clean_input(filename), self.clean_input(rz_name), self.clean_input(th_name))

          self.m_counter.increment()
          # print(img_no)
          q.put(sql_stmt)

      except Exception as e:
        print('Exception: ',  e, offset_count, self.m_pnum, filename)
        exit(0)

  def get_db_commit(self, offset_count, dict_path):

    geolocator = self.m_loc_interface.get_geopy()
    file_no = 0

    filenames = os.listdir(dict_path)
    # print(dict_path, len(filenames), self.m_db_name)
    for name in filenames:
      if os.path.isdir(dict_path + name):
        pass
        # print('  dir -> {0}'.format(dict_path + name))
        # break

      filename = dict_path + name
      if not os.path.isfile(filename):
        # print(' process: {0} {1}'.format(self.m_pnum, filename))
        continue

      _, ext = os.path.splitext(filename)

      if not (ext.lower() == '.jpg' or ext.lower() == '.jpeg'):
        # print(' process: {0} {1} {2}'.format(self.m_pnum, filename, ext))
        continue

      date, location, orientation, rz_name, th_name = self.m_loc_interface.get_picture_data(filename, geolocator)
      # date = format_date(date)
      # print(location)
      try:
        pos = filename.find(self.m_pic_path)
        assert pos != -1
        filename = filename[pos + len(self.m_pic_path):]
        img_no = offset_count + file_no
        # print('name: {0}\nfilename: {1}\nrz_name: {2}\nth_name: {3}'.format(name, filename, rz_name, th_name))
        sql_stmt = 'INSERT INTO PICTURE (ImageNo, Date, Location, Orientation, FileName, UrlOrg, UrlResize, UrlThumb) \
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s);' \
          % (img_no, self.clean_input(date), self.clean_input(str(location)), self.clean_input(str(orientation)),
          self.clean_input(name), self.clean_input(filename), self.clean_input(rz_name), self.clean_input(th_name))

        if img_no == 1727 or img_no == 470:
          # print('\t p_num {0} offset_count {1} file_no {2} {3}'.format(self.m_pnum, offset_count, file_no, img_no, filename))
          pass
        self.m_db_interface.execute(sql_stmt)
      except Exception as e:
        print('Exception: ',  e, offset_count, file_no, self.m_pnum, filename)
        break

      if self.m_max_download and file_no > self.m_max_download:
        assert False
        break
      file_no += 1

    try:
      self.m_db_interface.commit()
      # print('commited ', file_no)
    except Exception as e:
      print('Exception: ',  e, self.m_pnum, dict_path)

    return file_no

#####################################################################################
#
#                                   main
#
#####################################################################################

# otherwise just execute
if __name__ == "__main__":

  t_path = '/home/denis/Pictures/'
  filename = 'pc-pict/last day school bunker/IMG_1119.JPG'
  filename = 'pc-pict/ced au foot/IMG_1119.JPG'
  filename = 'pc-pict/iphone de zone/IMG_1119.JPG'
  filename = 'pc-pict/cefran 2017-randel/IMG_1646.JPG'

#  print(location)





#  basic_test(cursor)



