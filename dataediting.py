import pandas as pd

mydf=pd.read_csv("data2.csv")
print(mydf)
mydfdropna=mydf.dropna()
print(mydfdropna) # row 18 and 22 are deleted
mydf.dropna(inplace=True)
print(mydfdropna) # original data frame is changed
# some rows are deleted with "dropna"

mydffillna=pd.read_csv("data2.csv")
mydffillna.fillna({"Calories":190},inplace=True)
mydffillna.fillna({"Date":"'2020/11/30'"},inplace=True)
print(mydffillna)
# some rows are changed manually with method "fillna"

mydfmean=pd.read_csv("data2.csv")
calories_mean=mydfmean["Calories"].mean() # 304.68
mydfmean.fillna({"Calories":calories_mean},inplace=True)
print(mydfmean) # row 18 and 28 changed (calories)

mydfmedian=pd.read_csv("data2.csv")
calories_median=mydfmedian["Calories"].median() #  291.2
mydfmedian.fillna({"Calories":calories_median},inplace=True)
print(mydfmedian) # row 18 and 28 changed (calories)

mydfmode=pd.read_csv("data2.csv")
calories_mode=mydfmode["Calories"].mode()[0] #  300.0
mydfmode.fillna({"Calories":calories_mode},inplace=True)
print(mydfmode) # row 18 and 28 changed (calories)

# we will continue with mydfmean
print(mydfmean.duplicated()) # duplicated row will be True
mydfmean.drop_duplicates(inplace=True)
print(mydfmean) # row 12 is deleted