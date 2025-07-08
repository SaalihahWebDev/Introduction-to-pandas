import numpy as np
import pandas as pd

names=["Saalihah","Kashan","Shivangi"]
maths=np.array[80,70,90]
science=np.array[85,75,95]
data={
    "Name":names,
    "Maths":maths,
    "Science":science
}
df=pd.Dataframe(data)
df["Average"]=(df["Maths"])+(df["Science"])/2
print(df)