import pandas as pd

dataframe = pd.DataFrame(columns=["code"])
import re
x=[]
y=[]
w = " "
fr = open("EXTRACT2.txt", "r", encoding='utf-8')

for i in fr:
    w = w + i



x = re.findall('[^\w]+NCT0[\d]+', w)

for j in x:
    dataframe = dataframe.append ( {'code' : j} , ignore_index = True )

print(x)
print(len(x))

dataframe.to_excel("NTCOcodes"+str(len(x))+".xls",index = False)
fr.seek(0)
fr.close()
