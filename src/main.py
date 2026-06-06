import os
import numpy as np
import pandas as pd

data = np.random.rand(500, 10)
df = pd.DataFrame(data)

outpath = './output'
if not os.path.exists(outpath):
    os.makedirs(outpath)
outname = os.path.join(outpath, 'data.csv')

df.to_csv(outname, index=False)
print("File saved")
