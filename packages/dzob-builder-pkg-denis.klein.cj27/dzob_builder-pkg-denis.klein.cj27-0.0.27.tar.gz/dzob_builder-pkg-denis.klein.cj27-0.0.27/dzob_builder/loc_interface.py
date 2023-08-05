from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter

tiff_tag = [
  # TIFF Tag Reference, Baseline TIFF Tags, Image IFD
  (270,	'ImageDescription',	'A string that describes the subject of the image.'),
  (274,	'Orientation', 'The orientation of the image with respect to the rows and columns.'),
  (306,	'DateTime', 'Date and time of image creation.'),
  (315,	'Artist', 'Person who created the image.'),

  #  Exif IFD
  (36867, 'DateTimeOriginal', 'The date and time when the original image data was generated.'),
  (36868, 'DateTimeDigitized', 'The date and time when the image was stored as digital data.'),
  (37510, 'UserComment', 'Keywords or comments on the image; complements ImageDescription.'),
  (41728, 'FileSource', 'Indicates the image source.'),
  (41729, 'SceneType', 'Indicates the type of scene.')
]

# https://www.awaresystems.be/index.html
orientation_tag_list = [

  (1, 'Horizontal (normal)'),
  (2, 'Mirrored horizontal'),
  (3, 'Rotated 180'),
  (4, 'Mirrored vertical'),
  (5, 'Mirrored horizontal then rotated 90 CCW'),
  (6, 'Rotated 90 CW'),
  (7, 'Mirrored horizontal then rotated 90 CW'),
  (8, 'Rotated 90 CCW')

]

get_float = lambda x: float(x[0]) / float(x[1])

class Default(object):

  def __init__(self, *args):

    self.m_geolocator = None

  def get_geopy(self):

    return self.m_geolocator

  def get_picture_data(self, fname, geolocator):

    date = 'Unknown'
    location = 'Unknown'
    orientation = ''
    th_name = ''
    rz_name = ''

    # print('get_picture_data: ', fname)
    return date, location, orientation, rz_name, th_name

class GeoPy(object):

  def __init__(self, *args):

    self.m_args = args
    print(args)
    self.m_geolocator = Nominatim(user_agent = "zoby", timeout = 1)
    RateLimiter(self.m_geolocator.geocode, min_delay_seconds = 1)
    # geolocator = None

  def get_geopy(self):

    return self.m_geolocator

  def get_picture_data(self, fname, geolocator):

    _TAGS_r = dict(((v, k) for k, v in TAGS.items()))
    _GPSTAGS_r = dict(((v, k) for k, v in GPSTAGS.items()))

    date = 'Unknown'
    location = 'Unknown'
    orientation = ''
    th_name = ''
    rz_name = ''

    # print('get_picture_data: ', fname)
    # return date, location, orientation, rz_name, th_name
    try:
      img = Image.open(fname)
    except Exception as e:
      print('get_picture_data Image e: ', e)
      return date, location, orientation, rz_name, th_name

    if False:
      width, height = img.size
      w = int(width / 10)
      h = int(height / 10)
      rz_name = self.get_picture_thumbs(w, h, fname, '-resize.JPG', img)

      w = 128
      h = 128
      th_name = self.get_picture_thumbs(w, h, fname, '-thumb.JPG', img)

    exifd = img._getexif()  # as dict
    try:
      keys = list(exifd.keys())
    except:
      # print('image no keys found {0}'.format(fname))
      return date, 'geo-nokeys', orientation, rz_name, th_name

    keys = [k for k in keys if k in TAGS]
    if (37510) in keys:
      keys.remove(_TAGS_r["UserComment"])
    if (37500) in keys:
      keys.remove(_TAGS_r["MakerNote"])

    # symbolic name of keys
    for k in keys:
      val = exifd[k]
      res = type(val)
      if res == str:
        try:
          val = val.decode('utf-8')
        except:
          val = exifd[k]

      # print('{0} is {1}'.format(TAGS[k], val))
      if (TAGS[k] == 'DateTime'):
        date = val
      if (TAGS[k] == 'Orientation'):
        # orientation = val
        orientation = self.get_orientation_tag(val)
        if False:
          print('{0}'.format(fname))
          print('\t {0} is {1}'.format(orientation[0], orientation[1]))

    if (34853) not in keys:
      # print('not in keys: ', fname)
      return date, location, orientation, rz_name, th_name

    #print('{0} => {1}'.format(TAGS[34853], exifd[34853]))
    # exit(0)
    gpsinfo = exifd[_TAGS_r["GPSInfo"]]
    # print("\n gpsinfo ==")
    for k in gpsinfo.keys():
      # print('{0} => {1} => {2}'.format(k, GPSTAGS[k], gpsinfo[k]))
      pass

    lat, lon = self.get_lat_lon(exifd)
    if geolocator and lat != None and lon != None:
      coord = (lat, lon)
      try:
        location = geolocator.reverse(coord)
        # print('location: ', fname, ' ', location)
      except Exception as e:
        # print('geolocator error lat {0} lpn {1} {2} {3}'.format(lat, lon, fname, e))
        location = 'geo-error'

    return date, location, orientation, rz_name, th_name

  def get_orientation_tag(self, val):

    otag = [otag for otag in orientation_tag_list if otag[0] == val]

    return otag[0]

  def get_tag_value(self, key):

    for tag_data in tiff_tag:
      _, strg, _ = tag_data
      if key.find(strg) != -1:
        return True

    return False

  def convert_to_degrees(self, value):
    d = get_float(value[0])
    m = get_float(value[1])
    s = get_float(value[2])
    return d + (m / 60.0) + (s / 3600.0)

  def get_lat_lon(self, info):

    try:
      gps_latitude = info[34853][2]
      gps_latitude_ref = info[34853][1]
      gps_longitude = info[34853][4]
      gps_longitude_ref = info[34853][3]
      lat = self.convert_to_degrees(gps_latitude)
      if gps_latitude_ref != "N":
        lat *= -1

      lon = self.convert_to_degrees(gps_longitude)
      if gps_longitude_ref != "E":
        lon *= -1
      return lat, lon

    except KeyError:
  #    print('KeyError: ', info[34853])
      return None, None

  def get_picture_thumbs(self, w, h, fname, f_ext, img):

    pos = fname.find('.')
    rname = fname[:pos]

    pos = fname.find(h_path)
    assert pos != -1
    th_name = fname[pos + len(h_path) : ]
    pos = th_name.find('.')
    assert pos != -1
    th_name = th_name[ : pos]
    th_name = th_name + '-'+ str(w) + 'x' + str(h) + f_ext

    try:
      img_d = img.resize((w, h), Image.BICUBIC)
    except Exception as e:
      print('get_picture_thumbs fname {0} e: {1} '.format(fname, e))
      return ''

    rname = rname + '-'+ str(w) + 'x' + str(h) + f_ext
  # print('{0} w {1} h {2} sz: {3}'.format(rname, w, h, f_ext))
    img_d.save(rname)
    img_d.close()
  #  print('th_name {0} rname {1}'.format(th_name, rname))

    return th_name


###############################################################################################################
#
###############################################################################################################

if __name__ == "__main__":

  geolocator = Nominatim(user_agent="specify_your_app_name_here")
  location = geolocator.geocode("175 5th Avenue NYC")
  print(location.address)