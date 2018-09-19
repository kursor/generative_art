#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 14:39:40 2018

@author: aaronpenne
"""

import os

import numpy as np
np.random.seed(1138)

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import get_test_data


def check_dir(directory):
    if not os.path.isdir(directory):
        print('Creating ' + directory)
        os.mkdir(directory)
        
output_dir = 'output'
chart_dir = 'hmm'

check_dir(output_dir)
check_dir(os.path.join(output_dir, chart_dir))

fig = plt.figure(figsize=(4,4), 
                 dpi=100, 
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
#ax.axim = None
#ax.elev = None
ax.set_facecolor('#F1A9A0')

size = (100, 100)
X, Y, Z = get_test_data(0.01)
ax.plot_wireframe(X, Y, Z, 
                  rstride=10, 
                  cstride=10,
                  alpha=0.5,
                  color='#E26A6A')


for angle in np.arange(0, 360+1, 5):
    print(angle)
    
    fig = plt.figure(figsize=(4,4), 
                     dpi=100, 
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
    #ax.axim = None
    #ax.elev = None
    ax.set_facecolor('#F1A9A0')
    
    size = (100, 100)
    X, Y, Z = get_test_data(0.01)
    ax.plot_wireframe(X, Y, Z, 
                      rstride=10, 
                      cstride=10,
                      alpha=0.5,
                      color='#E26A6A')
    ax.view_init(90, angle)
    chart_filename = os.path.join(output_dir, chart_dir, 'azim_' + str(angle) + '.png')
    plt.savefig(chart_filename, dpi=fig.dpi)
    plt.close(fig)
    
    
for angle in np.arange(0, 360+1, 5):
    print(angle)
    
    fig = plt.figure(figsize=(4,4), 
                     dpi=100, 
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
    #ax.axim = None
    #ax.elev = None
    ax.set_facecolor('#F1A9A0')
    
    size = (100, 100)
    X, Y, Z = get_test_data(0.01)
    ax.plot_wireframe(X, Y, Z, 
                      rstride=10, 
                      cstride=10,
                      alpha=0.5,
                      color='#E26A6A')
    ax.view_init(angle, 90)
    chart_filename = os.path.join(output_dir, chart_dir, 'elev_' + str(angle) + '.png')
    plt.savefig(chart_filename, dpi=fig.dpi)
    plt.close(fig)
    