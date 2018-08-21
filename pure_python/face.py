#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 14:39:40 2018

@author: aaronpenne
"""

import numpy as np
np.random.seed(1138)


import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import get_test_data

fig = plt.figure(figsize=(4,4), 
                 dpi=300, 
                 facecolor=None, 
                 edgecolor=None, 
                 linewidth=0.0, 
                 frameon=False, 
                 subplotpars=None, 
                 tight_layout=None, 
                 constrained_layout=None)

ax = fig.add_subplot(111,
                     projection='3d', 
                     polar=False)

ax.axis('off')
ax.view_init(80, 90)
ax.set_facecolor('#F1A9A0')

size = (100, 100)
X, Y, Z = get_test_data(0.01)
ax.plot_wireframe(X, Y, Z, 
                  rstride=10, 
                  cstride=10,
                  alpha=0.5,
                  color='#E26A6A')

plt.show()
