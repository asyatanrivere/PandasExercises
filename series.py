import pandas as pd
import numpy as np
print(pd.__version__) # 3.0.2

numbers=[25,23,66,27,75,42]
seri=pd.Series(numbers, index=["a","b","c","d","e","f"])
print(seri)
"""
a    25
b    23
c    66
d    27
e    75
f    42
dtype: int64"""
seri2=pd.Series(numbers)
print(seri2)
"""
0    25
1    23
2    66
3    27
4    75
5    42
dtype: int64"""
itsme=["Asya","Tanrıvere","computer engineering",18,11,2004,]
series=pd.Series(itsme, index= [1,2,3,4,5,6])
print(series)
print(series[2])
"""
1                    Asya
2               Tanrıvere
3    computer engineering
4                      18
5                      11
6                    2004
dtype: object
Tanrıvere"""

mylist=list(range(1,101))
myindex=[f"option{i}" for i in range (1,101)]
result=pd.Series(mylist,index= myindex)
print(result.head(20))
print("\n")
"""
option1      1
option2      2
option3      3
option4      4
option5      5
option6      6
option7      7
option8      8
option9      9
option10    10
option11    11
option12    12
option13    13
option14    14
option15    15
option16    16
option17    17
option18    18
option19    19
option20    20
dtype: int64"""
print(result["option58"]) # 58
print(result.tail(5))
"""
option96      96
option97      97
option98      98
option99      99
option100    100"""
mynum=pd.Series(np.array([42,86,47,23,83])) # numpy array
print(mynum)
"""
0    42
1    86
2    47
3    23
4    83
dtype: int64"""
dailycalories={"day1":1385,"day2":1294,"day3":1348,"day4":1292}
calorieseries=pd.Series(dailycalories)
print(calorieseries)
"""
day1    1385
day2    1294
day3    1348
day4    1292
dtype: int64
"""
caloriespesific=pd.Series(dailycalories,index=["day1","day4"])
print(caloriespesific)
"""
day1    1385
day4    1292
dtype: int64
"""
# we can make a serie with tuples
tupleseries=pd.Series((2,5,4,6,7,12))
print(tupleseries)
"""
0     2
1     5
2     4
3     6
4     7
5    12
dtype: int64
"""
nums=[2,5,3,12,4,23,42,21]
numsseries=pd.Series(nums,index=[1,2,3,4,5,6,7,8])
print(numsseries.values)
# [ 2  5  3 12  4 23 42 21]
print(numsseries.index)
# Index([1, 2, 3, 4, 5, 6, 7, 8], dtype='int64')
print(numsseries.sum()) # 112
print(numsseries.min()) # 2
print(numsseries.max()) # 42
print(numsseries+10)
"""
1    12
2    15
3    13
4    22
5    14
6    33
7    52
8    31
dtype: int64
"""
print(numsseries*2)
"""
1     4
2    10
3     6
4    24
5     8
6    46
7    84
8    42
dtype: int64
"""
print(numsseries[numsseries>10])
"""
4    12
6    23
7    42
8    21
dtype: int64
"""
missingserie=pd.Series([3,np.nan,4])
print(missingserie)
"""
0    3.0
1    NaN
2    4.0
dtype: float64
"""
print(missingserie.isnull())
"""
0    False
1     True
2    False
dtype: bool
if the value is null, returns true """
print(missingserie.notnull())
"""
0     True
1    False
2     True
dtype: bool
if the value is null, returns FALSE """
print(missingserie[missingserie.notnull()])
"""
0    3.0
2    4.0
dtype: float64
"""