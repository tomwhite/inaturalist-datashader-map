import json
import sys

from colorcet import bmw
import dask
import pandas as pd
import datashader as ds
from datashader import transfer_functions as tf
from datashader.utils import lnglat_to_meters as webm
from datashader_fix.tiles import render_tiles # use version of render tiles with this fix: https://github.com/holoviz/datashader/pull/874

# The threads scheduler is more efficient than the multiprocessor one (which is the default for dask.bag)
# See https://docs.dask.org/en/latest/setup/single-machine.html
dask.config.set(scheduler='threads')

df = pd.read_csv('./data/inaturalist.csv')

def get_extents(df, x, y):
    return df[x].min(), df[y].min(), df[x].max(), df[y].max()

def load_data_func(x_range, y_range):
    return df.loc[df['x'].between(*x_range) & df['y'].between(*y_range)]

def rasterize_func(df, x_range, y_range, height, width):
    cvs = ds.Canvas(x_range=x_range, y_range=y_range,
                    plot_height=height, plot_width=width)
    agg = cvs.points(df, 'x', 'y')
    return agg

def shader_func(agg, span=None):
    img = tf.shade(agg, cmap=bmw, how='log', span=span)
    return img

def post_render_func(img, **kwargs):
    return img

if __name__ == '__main__':
    output_path = 'tiles'
    full_extent_of_data = get_extents(df, 'x', 'y')
    results = render_tiles(full_extent_of_data,
                        range(1, 7),
                        load_data_func=load_data_func,
                        rasterize_func=rasterize_func,
                        shader_func=shader_func,
                        post_render_func=post_render_func,
                        output_path=output_path)

