import linecache
from linecache_data import *

filename = make_tempfile()

print('Blank: {!r}'.format(linecache.getline(filename, 8)))
cleanup(filename)
