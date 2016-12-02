#!/usr/bin/env python

### We meant for you to encapsulate it in a function that takes an argument with the
### county, but you made it into a standalone script that takes a parameter from the
### command line. Great job!!!

import os
import sys
import glob
import pandas as pd
from matplotlib import pyplot

if len(sys.argv) != 2:
    print("usage: %s COUNTY" % sys.argv[0])
    sys.exit(1)

county = sys.argv[1]
data = []

for f in glob.glob('*.csv'):
    year, _ = os.path.splitext(os.path.basename(f))
    year = int(year)
    header = pd.read_csv(f, nrows = 1).dropna(axis = 1)
    d = header.iloc[0].to_dict()

    df = pd.read_csv(f, index_col = 0, thousands = ",", skiprows = [1])
    df.rename(inplace = True, columns = d)
    df.dropna(inplace = True, axis = 1)
    df["Year"] = year

    data.append(df[["Democratic", "Republican", "Total Votes Cast", "Year"]])

merged_data = pd.concat(data)
merged_data["Republican Vote Share"] = merged_data["Republican"] / merged_data["Total Votes Cast"]

plot = merged_data.loc["%s County" % county].plot(x="Year", y="Republican Vote Share")
plot.get_figure().savefig('%s.png' % county.lower().replace (" ", "_"))
