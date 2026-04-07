import pandas as pd
import numpy as np
print(pd.__version__)

numbers=[25,23,66,27,75,42]
seri=pd.Series(numbers, index=["a","b","c","d","e","f"])

print(seri)

itsme=["Asya","Tanrıvere","computer engineering",18,11,2004,]
series=pd.Series(itsme, index= [1,2,3,4,5,6])

print(series)
print(series[2])

mylist=list(range(1,101))
myindex=[f"option{i}" for i in range (1,101)]
result=pd.Series(mylist,index= myindex)
print(result.head(20))
print("\n")

mynum=pd.Series(np.array([42,86,47,23,83])) # numpy array
print(mynum)