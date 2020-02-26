import pandas as pd
from datashader.utils import lnglat_to_meters as webm

with open('data/inaturalist.csv', 'w') as f:
    f.write('x,y\n')
    for chunk in pd.read_csv("data/observations.csv", chunksize=10000):
        txt = ''
        for lng, lat in zip(chunk['decimalLongitude'], chunk['decimalLatitude']):
            txt += "%s,%s\n" % webm(lng, lat)
        f.write(txt)
