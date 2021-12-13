import numpy as np
import pandas as pd
from helpers import read_vars1
import matplotlib.pyplot as plt

if __name__ == '__main__':
    #define input spreadsheet
    cables_LH = 'cable_LH_readin.xlsx'
    #sheet names
    nsheet = ['Export HVAC', 'Array HVAC']
    ex_range = [132, 245, 300, 362, 420]
    ar_range = [66, 132, 150, 220, 275]

    #read through sheets
    cable_sheets = {}
    for s in nsheet:
        if 'Export' in s:
            cable_sheets[s] = read_vars1(file=cables_LH, sheet=s, xrange=ex_range)
        else:
            cable_sheets[s] = read_vars1(file=cables_LH, sheet=s, xrange=ar_range)


    #####generate plots
    
