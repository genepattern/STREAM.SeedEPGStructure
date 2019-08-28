#!/usr/bin/env python
# -*- coding: utf-8 -*-

import warnings

warnings.filterwarnings('ignore')

__tool_name__='STREAM'
print('''
   _____ _______ _____  ______          __  __ 
  / ____|__   __|  __ \|  ____|   /\   |  \/  |
 | (___    | |  | |__) | |__     /  \  | \  / |
  \___ \   | |  |  _  /|  __|   / /\ \ | |\/| |
  ____) |  | |  | | \ \| |____ / ____ \| |  | |
 |_____/   |_|  |_|  \_\______/_/    \_\_|  |_|
... Structure learning                                               
''',flush=True)

import stream as st
import argparse
import multiprocessing
import os
from slugify import slugify
import networkx as nx
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib as mpl
import sys

mpl.use('Agg')
mpl.rc('pdf', fonttype=42)

os.environ['KMP_DUPLICATE_LIB_OK']='True'


print('- STREAM Single-cell Trajectory Reconstruction And Mapping -',flush=True)
print('Version %s\n' % st.__version__,flush=True)
    

def main():
    sns.set_style('white')
    sns.set_context('poster')
    parser = argparse.ArgumentParser(description='%s Parameters' % __tool_name__ ,formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-m", "--data-file", dest="input_filename",default = None, help="input file name, pkl format from Stream preprocessing module", metavar="FILE")
    parser.add_argument("-of","--of",dest="output_filename_prefix", default="StreamiFSOutput",  help="output file name prefix")

    parser.add_argument("-nb_pct","--percent_neighbor_cells",dest="nb_pct", type=float, default=0.1, help="")
    parser.add_argument("-n_clusters",dest="n_clusters", type = int, default=10,  help="")
    parser.add_argument("-damping",dest="damping", type=float, default=0.75,   help="")
    parser.add_argument("-pref_perc",dest="pref_perc", type=int, default=50,   help="")
    parser.add_argument("-max_n_clusters",dest="max_n_clusters", type=int, default=200,   help="")

    parser.add_argument("-clustering",dest="clustering",  default='kmeans',  help="")
    
    parser.add_argument("-comp1",dest="comp1", type = int, default=0,  help="")   
    parser.add_argument("-comp2",dest="comp2", type = int, default=1,  help="")      
    parser.add_argument("-n_comp",dest="n_comp", type = int, default=3,  help="")      


    parser.add_argument("-fig_name",dest="fig_name",  default=None, help="")
    parser.add_argument("-fig_width",dest="fig_width", type=int, default=8, help="")        
    parser.add_argument("-fig_height",dest="fig_height", type=int, default=8, help="")
    parser.add_argument("-fig_legend_ncol",dest="fig_legend_ncol", type=int, default=None, help="")                                   


    args = parser.parse_args()
    
    print('Starting validation procedure...')
    workdir = "./"

    adata = st.read(file_name=args.input_filename, file_format='pkl', experiment='rna-seq', workdir=workdir)

    st.seed_elastic_principal_graph(adata, clustering=args.clustering, n_clusters=args.n_clusters, damping=args.damping, pref_perc=args.pref_perc,  max_n_clusters=args.max_n_clusters, nb_pct=args.nb_pct)
    st.plot_branches(adata, n_components=args.n_comp, comp1=args.comp1, comp2=args.comp2, save_fig=True, fig_name=(args.output_filename_prefix +'branches.png'), fig_path=None,fig_size=(args.fig_width, args.fig_height))
    st.plot_branches_with_cells(adata,n_components=args.n_comp,comp1=args.comp1,comp2=args.comp2, save_fig=True,fig_name=(args.output_filename_prefix +'branches_with_cells.png'),fig_path=None,fig_size=(args.fig_width, args.fig_height),fig_legend_ncol=args.fig_legend_ncol)

    st.write(adata,file_name=(args.output_filename_prefix + '_stream_result.pkl'),file_path='./',file_format='pkl') 

    print('Finished computation.')

if __name__ == "__main__":
    main()
