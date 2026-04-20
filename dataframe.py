import numpy as np
import pandas as pd

nameandage=[["Asya",21],["Ekin",19],["Lina",18],["Zeynep",20]]
dfnameandage=pd.DataFrame(nameandage,columns=["Names","Ages"],index=[1,2,3,4])
print(dfnameandage)
"""
    Names  Ages
1    Asya    21
2    Ekin    19
3    Lina    18
4  Zeynep    20
"""
nameandcity={
    "Names":["John","Jane","Christine","Christ","Anastasia"],
    "Cities":["Berlin","Paris","İstanbul","Denver","Montreal"],
    "Ages":[12,43,23,44,27]}
dfnameandcity=pd.DataFrame(nameandcity)
print(dfnameandcity)
"""
       Names    Cities  Ages
0       John    Berlin    12
1       Jane     Paris    43
2  Christine  İstanbul    23
3     Christ    Denver    44
4  Anastasia  Montreal    27
"""
schindlerslist={
    "Names":[f"Name{i}" for i in range(1,51)],
    "Cities":[f"City{i}" for i in np.random.randint(300,size=50)+1],
    "Ages":[i for i in np.random.randint(100,size=50)+1],
    "Number of siblings":[i for i in np.random.randint(15,size=50)]
}
dfschindlerslist=pd.DataFrame(schindlerslist)
print(dfschindlerslist.head(5))
"""
   Names   Cities  Ages  Number of siblings
0  Name1  City187    43                   4
1  Name2  City233    87                   5
2  Name3  City205    47                   6
3  Name4  City214    21                   1
4  Name5  City175    94                  11
"""
print(dfschindlerslist.tail(5))
"""
     Names   Cities  Ages  Number of siblings
45  Name46  City221    77                   2
46  Name47  City272    81                   0
47  Name48  City195    44                  11
48  Name49   City40     4                   2
49  Name50  City105   100                  14
"""
print(dfschindlerslist.shape) # (50, 4)
print(dfschindlerslist.columns)
# Index(['Names', 'Cities', 'Ages', 'Number of siblings'], dtype='str')
print(dfschindlerslist.index)
# RangeIndex(start=0, stop=50, step=1)
print(dfschindlerslist.dtypes)
"""
Names                   str
Cities                  str
Ages                  int32
Number of siblings    int32
dtype: object
"""
print(dfschindlerslist["Cities"])
"""
0     City102
1      City86
2      City22
3      City68
4     City117
5     City190
6      City97
7      City87
8      City97
9     City167
10     City22
11    City148
12    City244
13     City86
14     City70
15    City242
16     City96
17     City77
18    City175
19    City134
20    City159
21    City160
22     City53
23    City125
24    City155
25     City78
26    City259
27    City204
28     City11
29    City167
30    City170
31    City270
32     City62
33    City141
34    City142
35    City109
36    City237
37     City44
38    City157
39    City217
40     City20
41    City229
42    City129
43    City130
44    City103
45     City42
46     City32
47     City53
48    City272
49    City115"""
print(dfschindlerslist[["Cities","Ages"]])
"""
     Cities  Ages
0   City102    91
1    City86    36
2    City22    21
3    City68    50
4   City117    91
5   City190    85
6    City97    71
7    City87    64
8    City97    81
9   City167    10
10   City22    94
11  City148    79
12  City244    97
13   City86    52
14   City70    96
15  City242    90
16   City96   100
17   City77    15
18  City175    70
19  City134    37
20  City159    47
21  City160    10
22   City53    70
23  City125    89
24  City155    80
25   City78    34
26  City259    55
27  City204    77
28   City11    22
29  City167    62
30  City170    72
31  City270     9
32   City62     4
33  City141    43
34  City142    29
35  City109    70
36  City237    68
37   City44    42
38  City157     3
39  City217    95
40   City20    80
41  City229    50
42  City129     7
43  City130    23
44  City103    67
45   City42    41
46   City32    66
47   City53    58
48  City272    86
49  City115    27
"""
print(dfschindlerslist.loc[5])
"""
Names                   Name6
Cities                City289
Ages                       70
Number of siblings         13
Name: 5, dtype: object
"""
print(dfschindlerslist.loc[[4,8]])
"""
   Names   Cities  Ages  Number of siblings
4  Name5  City253    21                   4
8  Name9  City114     7                  12
"""
print("--------------------------------------")
print(dfschindlerslist[dfschindlerslist["Ages"]>65])
"""
     Names   Cities  Ages  Number of siblings
2    Name3  City254    91                   1
5    Name6  City236    78                   6
7    Name8  City267    91                  12
12  Name13   City11    69                   1
16  Name17  City292    83                  14
20  Name21   City39    66                   7
22  Name23  City279    80                   3
24  Name25  City179    70                   8
25  Name26  City109    93                   1
27  Name28  City282    70                   5
31  Name32  City274    79                  13
33  Name34  City133    79                  13
40  Name41   City58    91                   0
41  Name42   City66    72                  14
42  Name43  City232    87                  12
43  Name44  City161    86                   5
47  Name48  City284    89                  10
48  Name49   City40    88                   9
49  Name50  City259    85                  10
"""
coffeeorder={
    "coffee":["americano","latte","mocha","flat white","cortado"],
    "price":[100,120,130,125,115],
    "amount":[3,2,4,1,1]
}
dfcoffeeorder=pd.DataFrame(coffeeorder)
dfcoffeeorder["income"]=dfcoffeeorder["price"]*dfcoffeeorder["amount"]
print(dfcoffeeorder)
"""
       coffee  price  amount  income
0   americano    100       3     300
1       latte    120       2     240
2       mocha    130       4     520
3  flat white    125       1     125
4     cortado    115       1     115
"""