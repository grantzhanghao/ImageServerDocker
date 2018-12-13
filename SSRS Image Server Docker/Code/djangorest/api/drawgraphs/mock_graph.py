from matplotlib import pylab
from pylab import plt,xlabel,ylabel,grid
from PIL import Image
from io import BytesIO
import base64
from api.utils import get_translate_string, get_own_defined_font
import pandas as pd
from math import sqrt
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from matplotlib.collections import EventCollection
from datetime import datetime
font = None

def draw_mock_graph():
    '''draw the toe energy per meter graph.
    '''
    plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
    plt.axis([0, 6, 0, 20])
    
    canvas = pylab.get_current_fig_manager().canvas
    canvas.draw()
    pil_image = Image.frombytes("RGB", canvas.get_width_height(), canvas.tostring_rgb())
    pylab.close()
    return pil_image
