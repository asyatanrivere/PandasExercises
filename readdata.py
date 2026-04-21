import pandas as pd

healthdf=pd.read_csv("data.csv")
"""in some cases:
delimiter=";", encoding="utf-8" 
"""
print(healthdf)
"""
     Duration  Pulse  Maxpulse  Calories
0          60    110       130     409.1
1          60    117       145     479.0
2          60    103       135     340.0
3          45    109       175     282.4
4          45    117       148     406.0
..        ...    ...       ...       ...
164        60    105       140     290.8
165        60    110       145     300.0
166        60    115       145     310.2
167        75    120       150     320.4
168        75    125       150     330.4

[169 rows x 4 columns]
"""
#print(healthdf.to_string()) 
# returns all data frame
# all the 168 row of data

print(healthdf.head())
"""
   Duration  Pulse  Maxpulse  Calories
0        60    110       130     409.1
1        60    117       145     479.0
2        60    103       135     340.0
3        45    109       175     282.4
4        45    117       148     406.0
"""
#print(healthdf.to_string()) -> prints all the data
print(pd.options.display.max_rows) # 60
#pd.options.display.max_rows=200
#print(pd.options.display.max_rows) # 200
# we can get 200 rows of data

jsonurl="https://www.w3schools.com/python/pandas/data.js"
jsondf=pd.read_json(jsonurl)
print(jsondf)
"""
     Duration  Pulse  Maxpulse  Calories
0          60    110       130     409.1
1          60    117       145     479.0
2          60    103       135     340.0
3          45    109       175     282.4
4          45    117       148     406.0
..        ...    ...       ...       ...
164        60    105       140     290.8
165        60    110       145     300.4
166        60    115       145     310.2
167        75    120       150     320.4
168        75    125       150     330.4

[169 rows x 4 columns]
"""
pathbook=pd.read_csv("Books.csv")
print(pathbook.head(20))
print(pathbook[["ISBN","Book-Title","Book-Author","Year-Of-Publication"]].head(20))
"""
          ISBN                                         Book-Title           Book-Author Year-Of-Publication
0   0195153448                                Classical Mythology    Mark P. O. Morford                2002
1   0002005018                                       Clara Callan  Richard Bruce Wright                2001
2   0060973129                               Decision in Normandy          Carlo D'Este                1991
3   0374157065  Flu: The Story of the Great Influenza Pandemic...      Gina Bari Kolata                1999
4   0393045218                             The Mummies of Urumchi       E. J. W. Barber                1999
5   0399135782                             The Kitchen God's Wife               Amy Tan                1991
6   0425176428  What If?: The World's Foremost Military Histor...         Robert Cowley                2000
7   0671870432                                    PLEADING GUILTY           Scott Turow                1993
8   0679425608  Under the Black Flag: The Romance and the Real...       David Cordingly                1996
9   074322678X            Where You'll Find Me: And Other Stories           Ann Beattie                2002
10  0771074670                        Nights Below Station Street  David Adams Richards                1988
11  080652121X  Hitler's Secret Bankers: The Myth of Swiss Neu...            Adam Lebor                2000
12  0887841740                                 The Middle Stories           Sheila Heti                2004
13  1552041778                                           Jane Doe          R. J. Kaiser                1999
14  1558746218  A Second Chicken Soup for the Woman's Soul (Ch...         Jack Canfield                1998
15  1567407781       The Witchfinder (Amos Walker Mystery Series)     Loren D. Estleman                1998
16  1575663937  More Cunning Than Man: A Social History of Rat...    Robert Hendrickson                1999
17  1881320189                      Goodbye to the Buttermilk Sky          Julia Oliver                1994
18  0440234743                                      The Testament          John Grisham                1999
19  0452264464               Beloved (Plume Contemporary Fiction)         Toni Morrison                1994
"""
pd.set_option("display.max_columns",None)#  no limit, shows ALL COLUMNS
print(pathbook.head(20))
print("-----------------------------------------------")
print(pathbook["Year-Of-Publication"].dtype) # object
pathbook["Year-Of-Publication"] = pd.to_numeric(pathbook["Year-Of-Publication"], errors="coerce")
print((pathbook[pathbook["Year-Of-Publication"]>2000]).head())