# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 12:34:46 2020

@author: jawessel
"""

from pyomo.opt import SolverFactory
from CA_dispatch import model as m1
from CA_dispatchLP import model as m2
from pyomo.core import Var
from pyomo.core import Constraint
from pyomo.core import Param
from operator import itemgetter
import pandas as pd
import numpy as np
from datetime import datetime
import pyomo.environ as pyo


#def grab_mins(path, region, sim_year, year):
def grab_mins(region):

    #Define focus
    #path = 'EV', 'MID', 'BAT', 'LOWRECOST', or 'HIGHRECOST'
    #region = 'CA' or 'PNW'
    #year = 2020, 2025, 2030, 2035, 2040, 2045, or 2050 passed as an integer, not string
    #sim_year = int from 0 to 99

    #Initialize empty list to populate with hourly values
    import_mins = []
    export_demand = []

    #Find data file and create instance of model
#    filename = '{}/data/{}_{}/{}{}/data.dat'.format(path,path,str(year),region,str(sim_year))
    filename = 'data.dat'
    instance = m1.create_instance(filename)

    if region == 'CA':
        for j in range(1,8761):
            mins_sum = instance.SimPath46_SCE_imports_minflow[j] + instance.SimPath66_imports_minflow[j] +\
                instance.SimPath42_imports_minflow[j] + instance.SimPath61_imports_minflow[j]
            export_demand_sum = instance.SimPath42_exports[j] + instance.SimPath24_exports[j] +\
                instance.SimPath45_exports[j] + instance.SimPath66_exports[j]
            import_mins.append(mins_sum)
            export_demand.append(export_demand_sum)

    if region == 'PNW':
        for j in range(1,8761):
            mins_sum = instance.SimPath3_imports_minflow[j] + instance.SimPath8_imports_minflow[j] +\
                instance.SimPath14_imports_minflow[j] + instance.SimPath65_imports_minflow[j] + instance.SimPath66_imports_minflow[j]
            export_demand_sum = instance.SimPath3_exports[j] + instance.SimPath8_exports[j] +\
                instance.SimPath14_exports[j] + instance.SimPath65_exports[j] + instance.SimPath66_exports[j]
            import_mins.append(mins_sum)
            export_demand.append(export_demand_sum)

    return import_mins, export_demand




