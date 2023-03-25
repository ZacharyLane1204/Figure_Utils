# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 15:28:49 2023

@author: porri
"""

import matplotlib.pyplot as plt
import numpy as np

def figure_size(size = 'column'):

    if size == 'column':
        size = 244.0
    elif size == 'page':
        size = 508.0

    plt.rc('text', usetex=True)
    plt.rc('font', family='serif')
    
    fig_width_pt = size  # Get this from LaTeX using \showthe\columnwidth
    
    inches_per_pt = 1.0/72.27               # Convert pt to inches
    
    golden_mean = (np.sqrt(5)-1.0)/2.0         # Aesthetic ratio
    
    fig_width = fig_width_pt*inches_per_pt  # width in inches
    
    fig_height = fig_width*golden_mean       # height in inches
    
    fig_size = [fig_width,fig_height]
    
    return fig_size

# x = np.linspace(0,1,101)

# fig_size = figure_size()

# plt.figure(figsize = fig_size)
# plt.plot(x,x)
# # plt.savefig('TEST.pdf', dpi = 1200, bbox_inches='tight' )
# plt.show()

# print((time.time()-start)/60)