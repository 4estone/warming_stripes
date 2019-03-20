# -*- coding: utf-8; -*-

import pandas as pd
import numpy as np

import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize

import os, sys
import requests, io


# inspired from https://github.com/fmaussion IPython notebook
# GISTEMP data from https://data.giss.nasa.gov/gistemp/tabledata_v3/GLB.Ts+dSST.csv


os.chdir('C:\Temp\climat')

savenameyear = 'global_temps_line_year'
savenamemonth = 'global_temps_line_month'

url = 'https://data.giss.nasa.gov/gistemp/tabledata_v3/GLB.Ts+dSST.csv'
response = requests.get(url)

# If you have the data, use:
# df = pd.read_csv('GLB.Ts+dSST.csv', header=1, skipfooter=1, engine='python')

df = pd.read_csv(io.StringIO(response.text), header=1, skipfooter=1, engine='python')
# Annual values only
dfa = df[['Year', 'J-D']].copy()

dfa.columns = ['Year', 'Anomaly']
# This is to trick holoviews into making an image out of the dataframe
dfa['index'] = 1
# We want to display the rank as well
dfa['Rank'] = len(dfa) - np.argsort(dfa['Anomaly'])

#dfa['Anomaly'].plot()

#fig, ws = plt.subplots()
#fig = plt.figure(figsize=(12,6))

plt.figure(figsize=(12,6))
plt.pcolormesh(dfa['Anomaly'].values.reshape((1, len(dfa))), cmap='RdBu_r')
plt.colorbar(format='%.1f°C')

plt.axis('off')
plt.axis('tight')
plt.ylim(0, 1)

plt.savefig(savenameyear+'.png', dpi=600)
sys.exit()

