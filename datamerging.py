import pandas as pd

people = {
    "isim": ["Asya","Ekin","Lina","Zeynep","Mert","Elif","Can"],
    "meslek": ["IT","IT","Proje Yöneticisi","Proje Yöneticisi","Makine Mühendisi","Analist","Analist"],
    "yas": [21,23,22,30,27,35,29],
    "sehir": ["İzmir","İzmir","İzmir","Bursa","Kocaeli","Antalya","Eskişehir"],
    "maas": [35000,35000,28000,40000,36000,50000,33000]
    }
df=pd.DataFrame(people)
print(df)
"""
     isim            meslek  yas      sehir   maas
0    Asya                IT   21      İzmir  35000
1    Ekin                IT   23      İzmir  35000
2    Lina  Proje Yöneticisi   22      İzmir  28000
3  Zeynep  Proje Yöneticisi   30      Bursa  40000
4    Mert  Makine Mühendisi   27    Kocaeli  36000
5    Elif           Analist   35    Antalya  50000
6     Can           Analist   29  Eskişehir  33000
"""
for name,group in df.groupby("sehir"):
    print("City name:",name)
    print(group,"\n")
"""
City name: Antalya
   isim   meslek  yas    sehir   maas
5  Elif  Analist   35  Antalya  50000 

City name: Bursa
     isim            meslek  yas  sehir   maas
3  Zeynep  Proje Yöneticisi   30  Bursa  40000 

City name: Eskişehir
  isim   meslek  yas      sehir   maas
6  Can  Analist   29  Eskişehir  33000 

City name: Kocaeli
   isim            meslek  yas    sehir   maas
4  Mert  Makine Mühendisi   27  Kocaeli  36000 

City name: İzmir
   isim            meslek  yas  sehir   maas
0  Asya                IT   21  İzmir  35000
1  Ekin                IT   23  İzmir  35000
2  Lina  Proje Yöneticisi   22  İzmir  28000 
"""

for name,group in df.groupby("meslek"):
    print("Department name:",name)
    print(group,"\n")
"""
Department name: Analist
   isim   meslek  yas      sehir   maas
5  Elif  Analist   35    Antalya  50000
6   Can  Analist   29  Eskişehir  33000 

Department name: IT
   isim meslek  yas  sehir   maas
0  Asya     IT   21  İzmir  35000
1  Ekin     IT   23  İzmir  35000 

Department name: Makine Mühendisi
   isim            meslek  yas    sehir   maas
4  Mert  Makine Mühendisi   27  Kocaeli  36000 

Department name: Proje Yöneticisi
     isim            meslek  yas  sehir   maas
2    Lina  Proje Yöneticisi   22  İzmir  28000
3  Zeynep  Proje Yöneticisi   30  Bursa  40000 
"""

dfsehir=df.groupby("sehir").get_group("İzmir")
print(dfsehir)
"""
   isim            meslek  yas  sehir   maas
0  Asya                IT   21  İzmir  35000
1  Ekin                IT   23  İzmir  35000
2  Lina  Proje Yöneticisi   22  İzmir  28000
"""
dfdepartment=df.groupby("meslek").get_group("IT")
print(dfdepartment)
"""
   isim meslek  yas  sehir   maas
0  Asya     IT   21  İzmir  35000
1  Ekin     IT   23  İzmir  35000
"""
dfdepartmentsalary=df.groupby("meslek")["maas"].sum()
print(dfdepartmentsalary)
"""
meslek
Analist             83000
IT                  70000
Makine Mühendisi    36000
Proje Yöneticisi    68000
Name: maas, dtype: int64
"""
dfdepartmentsalarymean=df.groupby("meslek")["maas"].mean()
print(dfdepartmentsalarymean)
"""
meslek
Analist             41500.0
IT                  35000.0
Makine Mühendisi    36000.0
Proje Yöneticisi    34000.0
Name: maas, dtype: float64
"""
dfdepartmentnamecount=df.groupby("meslek")["isim"].count()
print(dfdepartmentnamecount)
"""
meslek
Analist             2
IT                  2
Makine Mühendisi    1
Proje Yöneticisi    2
Name: isim, dtype: int64
"""
dfdepartmentagemax=df.groupby("meslek")["yas"].max()
print(dfdepartmentagemax)
"""
meslek
Analist             35
IT                  23
Makine Mühendisi    27
Proje Yöneticisi    30
Name: yas, dtype: int64"""
dfdepartmentagemin=df.groupby("meslek")["yas"].min()
print(dfdepartmentagemin)
"""
meslek
Analist             29
IT                  21
Makine Mühendisi    27
Proje Yöneticisi    22
Name: yas, dtype: int64
"""
dfitagemindf=df.groupby("meslek")["yas"].min()["IT"]
print(dfitagemindf) # 21

data1=pd.DataFrame({
    "id":[1,2,3],
    "name":["John","Maria","Gerard"]
})
data2=pd.DataFrame({
    "id":[1,2,4],
    "age":[23,55,48]
})
result=pd.merge(data1,data2,on="id")
print(result)
"""
   id   name  age
0   1   John   23
1   2  Maria   55
"""
data2_1=pd.DataFrame({
    "id":[1,2,3],
    "age":[23,55,48]
})
result2=pd.merge(data1,data2_1,on="id")
print(result2)
"""
   id    name  age
0   1    John   23
1   2   Maria   55
2   3  Gerard   48
"""
data3=pd.DataFrame({"name":["Leonardo","Jackson","Henry","Simon"]},index=[1,2,3,4])
data4=pd.DataFrame({"age":[23,43,37,27]},index=[1,2,3,5])
result3=data3.join(data4)
"""
print(result3)
       name   age
1  Leonardo  23.0
2   Jackson  43.0
3     Henry  37.0
4     Simon   NaN,
"""
data3_1=pd.DataFrame({"name":["Leonardo","Jackson","Henry","Simon"]},index=[1,2,3,4])
data4_1=pd.DataFrame({"age":[23,43,37,27]},index=[1,2,3,4])
result4=data3_1.join(data4_1)
print(result4)
# we don't have to write indexes, or it will begin from 0
"""
       name  age
1  Leonardo   23
2   Jackson   43
3     Henry   37
4     Simon   27
"""