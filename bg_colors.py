import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap

# Utilities:
def hex2map(hex):
    # Convert hex code to map input
    hex = hex[1:]
    rgb = tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))
    rgb = np.array(rgb)/255
    rgb = np.append(rgb,1)
    return rgb

# Linear Schemes:
def create_cmap_stack(hex_list):
    interpolation_list = []
    for i in range(0,len(hex_list)-1):
        interpolation_list.append(np.linspace(hex2map(hex_list[i]), hex2map(hex_list[i+1]), num=100))
    new_cmap = np.concatenate(interpolation_list,axis=0)
    return ListedColormap(new_cmap)       

def create_cmap_white(hex1,hex2):
    interpolated1 = np.linspace(hex2map(hex1), np.array([1,1,1,1]), num=100)
    interpolated2 = np.linspace(np.array([1,1,1,1]), hex2map(hex2), num=100)
    new_cmap = np.concatenate([interpolated1,interpolated2],axis=0)
    return ListedColormap(new_cmap)

# Skewed Schemes:
def interp_skew(v1,v2):
    t = np.sqrt(np.linspace(0, 1, 100))  # Skew toward 1
    t = t[:, None]

    interpolated = (1 - t) * v1 + t * v2
    return interpolated

def create_cmap_skew(hex1,hex2,hex3):
    interpolated1 = interp_skew(np.array(hex2map(hex2)),hex2map(hex1))
    interpolated2 = interp_skew(np.array(hex2map(hex2)),hex2map(hex3))
    interpolated1 = interpolated1[::-1]
    new_cmap = np.concatenate([interpolated1,interpolated2],axis=0)
    new_cmap = new_cmap[::-1]
    return ListedColormap(new_cmap)

def create_cmap_white_skew(hex1,hex2):
    interpolated1 = interp_skew(np.array([1,1,1,1]),hex2map(hex1))
    interpolated2 = interp_skew(np.array([1,1,1,1]),hex2map(hex2))
    interpolated1 = interpolated1[::-1]
    new_cmap = np.concatenate([interpolated1,interpolated2],axis=0)
    new_cmap = new_cmap[::-1]
    return ListedColormap(new_cmap)

class ColorScheme:
    def __init__(self):
        self.set_colors()
        self.set_default_cmaps()
        
    def set_colors(self):
        # Blues
        self.lb = '#8ABAD4'
        self.b = '#418AB3'
        self.db = '#316886'
        self.ddb = '#20455A'

        # Greens
        self.lg = '#D3E171'
        self.g = '#A6B727'
        self.dg = '#7D891D'
        self.ddg = '#535C13'

        # Reds
        self.lr = '#EC987D'
        self.r = '#DF5327'
        self.dr = '#AB3C19'
        self.ddr = '#722811'

        # Oranges
        self.lo = '#FFD495'
        self.o = '#F69200'
        self.do = '#B96D00'
        self.ddo = '#7B4900'

        # Yellows
        self.ly = '#FFE79B'
        self.y = '#FEC306'
        self.dy = '#C29401'
        self.ddy = '#816301'

        # Purples
        self.lp = '#EFBBFB'
        self.p = '#9F5CCE'
        self.dp = '#683C87'
        self.dp = '#512E6A'

    def set_default_cmaps(self):
        self.rwb_cm = create_cmap_white_skew(self.r,self.b)
        self.bwr_cm = create_cmap_white_skew(self.b,self.r)
        self.bwg_cm = create_cmap_white_skew(self.b,self.g)
        self.gwb_cm = create_cmap_white_skew(self.g,self.b)
        self.rwg_cm = create_cmap_white_skew(self.r,self.g)
        self.gwr_cm = create_cmap_white_skew(self.g,self.r)
        self.gbp_cm = create_cmap_skew(self.lg,self.b,self.dp)
        self.pbg_cm = create_cmap_skew(self.dp,self.b,self.lg)
        self.yrp_cm = create_cmap_skew(self.ly,self.r,self.dp)
        self.pry_cm = create_cmap_skew(self.dp,self.r,self.ly)
        self.rpb_cm = create_cmap_skew(self.r,self.lp,self.ddb)
        self.bpr_cm = create_cmap_skew(self.ddb,self.lp,self.r)


