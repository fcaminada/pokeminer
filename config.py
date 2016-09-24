# coding: utf-8
from datetime import datetime

DB_ENGINE = 'mysql://root:root@localhost/testmap'
ENCRYPT_PATH = '/home/fcaminada/Unicamp/pokeminer/libencrypt/libencrypt-linux-x86-64.so'

AREA_NAME = u'Unicamp'
LANGUAGE = 'EN'  # ISO 639-1 codes EN, DE, FR, and ZH currently supported.
MAP_START = (-22.800158, -47.084154)
MAP_END = (-22.833544, -47.034309)
GRID = (3,4)  # row, column
DISABLE_WORKERS = [0,1,2,3,10,11]
CYCLES_PER_WORKER = 5
SCAN_DELAY = 15  # seconds
PROXIES = None  # Insert dictionary with 'http' and 'https' keys to enable

SCAN_RADIUS = 80  # metres

ACCOUNTS = [
    ('fcpgo07', 'fefaogo07', 'ptc'),
    ('fcpgo08', 'fefaogo08', 'ptc'),
    ('fcpgo09', 'fefaogo09', 'ptc'),
    ('fcpgo10', 'fefaogo10', 'ptc'),
    ('fcpgo11', 'fefaogo11', 'ptc'),
    ('fcpgo12', 'fefaogo12', 'ptc'),
    ('fcpgo13', 'fefaogo13', 'ptc'),
    ('fcpgo14', 'fefaogo14', 'ptc'),
    ('fcpgo15', 'fefaogo15', 'ptc')
]

TRASH_IDS = [10, 13, 16, 19, 21, 23, 41, 46, 96, 133]

STAGE2 = [
  3, 6, 9, 31, 101, 87, 89, 91, 34, 38, 45, 51, 53, 82,
  59, 62, 65, 68, 71, 76, 78, 80, 94, 103, 105,
  106, 107, 112, 113, 117, 123, 124, 125, 126,
  130, 131, 137, 142, 143, 139, 141, 149
]

REPORT_SINCE = datetime(2016, 7, 29)
GOOGLE_MAPS_KEY = 's3cr3t'
MAP_PROVIDER_URL = '//{s}.tile.osm.org/{z}/{x}/{y}.png'
MAP_PROVIDER_ATTRIBUTION = '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
