import pandas as pd
import matplotlib.pyplot as plt

mydf=pd.read_csv("data2.csv")
mydf["Date"]=pd.to_datetime(mydf["Date"],format="mixed")
mydf.dropna(subset=["Date"],inplace=True)
# mydf.loc[7,"Duration"]=45 
# --> for big datasets, we'll use it:
for item in mydf.index:
    if mydf.loc[item,"Duration"]>60:
        mydf.loc[item,"Duration"]=50
        """
        OR
        mydf.drop(item,inplace=True)"""
print(mydf)
mydf2=pd.read_csv("data.csv")
print(mydf.corr())
"""
          Duration      Date     Pulse  Maxpulse  Calories
Duration  1.000000  0.189899 -0.091840 -0.303538  0.321659
Date      0.189899  1.000000 -0.360587 -0.502902 -0.352105
Pulse    -0.091840 -0.360587  1.000000  0.269000  0.510361
Maxpulse -0.303538 -0.502902  0.269000  1.000000  0.352529
Calories  0.321659 -0.352105  0.510361  0.352529  1.000000
"""
mydf2.plot(kind="scatter",x="Duration",y="Calories")
plt.show()