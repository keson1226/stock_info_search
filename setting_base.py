import os
import shutil

import matplotlib
import matplotlib.pyplot as plt

plt.title("title")
path=matplotlib.__path__[0]+"/mpl-data/fonts/ttf"
shutil.copy("TaipeiSansTCBeta-Regular.ttf",path)
os.remove(os.path.expanduser('~')+"/.matplotlib/fontlist-v330.json")