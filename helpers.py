import pandas as pd
import numpy as np

critmat_LH_ind = {
    'vltg_kV': 1,
    'insltn_630mm': 2,
    'insltn_d_630mm': 3,
    'Pb_630mm': 4,
    'outer_d_630mm': 5,
    'mass_630kg_m': 6,
    'insltn_800mm': 11,
    'insltn_d_800mm': 12,
    'Pb_800mm': 13,
    'outer_d_800mm': 14,
    'mass_800kg_m': 15,
    'insltn_1000mm': 20,
    'insltn_d_1000mm': 21,
    'Pb_1000mm': 22,
    'outer_d_1000mm': 23,
    'mass_1000kg_m': 24,
    'insltn_1200mm': 29,
    'insltn_d_1200mm': 30,
    'Pb_1200mm': 31,
    'outer_d_1200mm': 32,
    'mass_1200kg_m': 33,
    'col': 1,

}

def read_vars1(file, sheet, xrange, header=1, cols='B:G', rows=40, ind=critmat_LH_ind):
    df = pd.read_excel(file, sheet_name=sheet, header=header, usecols=cols, nrows=rows)
    # Extract all required variables as numpy arrays
    _vltg_kV = df.iloc[ind['vltg_kV'], ind['col']:ind['col'] + len(xrange) ].to_numpy()
    _insltn_630mm = df.iloc[ind['insltn_630mm'], ind['col']:ind['col'] + len(xrange)].to_numpy()
    _insltn_d_630mm = df.iloc[ind['insltn_d_630mm'], ind['col']:ind['col']+len(xrange)].to_numpy()
    _Pb_630mm = df.iloc[ind['Pb_630mm'], ind['col']:ind['col']+len(xrange)].to_numpy()
    _outer_d_630mm = df.iloc[ind['outer_d_630mm'], ind['col']:ind['col'] + len(xrange)].to_numpy()
    _mass_630kg_m = df.iloc[ind['mass_630kg_m'], ind['col']:ind['col'] + len(xrange)].to_numpy()
    _insltn_800mm = df.iloc[ind['insltn_800mm'], ind['col']:ind['col'] + len(xrange)].to_numpy()
    _insltn_d_800mm = df.iloc[ind['insltn_d_800mm'], ind['col']:ind['col']+len(xrange)].to_numpy()
    _Pb_800mm = df.iloc[ind['Pb_800mm'], ind['col']:ind['col']+len(xrange)].to_numpy()
    _outer_d_800mm = df.iloc[ind['outer_d_800mm'], ind['col']:ind['col'] + len(xrange)].to_numpy()
    _mass_800kg_m = df.iloc[ind['mass_800kg_m'], ind['col']:ind['col'] + len(xrange)].to_numpy()
    _insltn_1000mm = df.iloc[ind['insltn_1000mm'], ind['col']:ind['col'] + len(xrange)].to_numpy()
    _insltn_d_1000mm = df.iloc[ind['insltn_d_1000mm'], ind['col']:ind['col']+len(xrange)].to_numpy()
    _Pb_1000mm = df.iloc[ind['Pb_1000mm'], ind['col']:ind['col']+len(xrange)].to_numpy()
    _outer_d_1000mm = df.iloc[ind['outer_d_1000mm'], ind['col']:ind['col'] + len(xrange)].to_numpy()
    _mass_1000kg_m = df.iloc[ind['mass_1000kg_m'], ind['col']:ind['col'] + len(xrange)].to_numpy()
    _insltn_1200mm = df.iloc[ind['insltn_1200mm'], ind['col']:ind['col'] + len(xrange)].to_numpy()
    _insltn_d_1200mm = df.iloc[ind['insltn_d_1200mm'], ind['col']:ind['col']+len(xrange)].to_numpy()
    _Pb_1200mm = df.iloc[ind['Pb_1200mm'], ind['col']:ind['col']+len(xrange)].to_numpy()
    _outer_d_1200mm = df.iloc[ind['outer_d_1200mm'], ind['col']:ind['col'] + len(xrange)].to_numpy()
    _mass_1200kg_m = df.iloc[ind['mass_1200kg_m'], ind['col']:ind['col'] + len(xrange)].to_numpy()
    #hbjbhhb
    _out1 = {
            'vltg_kV': _vltg_kV,
            'insltn_630mm': _insltn_630mm,
            'insltn_d_630mm': _insltn_d_630mm,
            'Pb_630mm': _Pb_630mm,
            'outer_d_630mm': _outer_d_630mm,
            'mass_630kg_m': _mass_630kg_m,
            'insltn_800mm': _insltn_800mm,
            'insltn_d_800mm': _insltn_d_800mm,
            'Pb_800mm': _Pb_800mm,
            'outer_d_800mm': _outer_d_800mm,
            'mass_800kg_m': _mass_800kg_m,
            'insltn_1000mm': _insltn_1000mm,
            'insltn_d_1000mm': _insltn_d_1000mm,
            'Pb_1000mm': _Pb_1000mm,
            'outer_d_1000mm': _outer_d_1000mm,
            'mass_1000kg_m': _mass_1000kg_m,
            'insltn_1200mm': _insltn_1200mm,
            'insltn_d_1200mm': _insltn_d_1200mm,
            'Pb_1200mm': _Pb_1200mm,
            'outer_d_1200mm': _outer_d_1200mm,
            'mass_1200kg_m': _mass_1200kg_m,

        }
    return _out1
