from os import linesep
from types import resolve_bases
import pandas as pd
import plotly.express as px
import csv
import math
with open('SD.csv',newline='') as f:
    read=csv.reader(f)
    fileData=list(read)

newData=fileData[0]

def mean(data):
    n=len(data)
    sum=0

    for x in data:
        sum+=int(x)
    
    mean=sum/n

    return mean

squareList=[]
for x in newData:
    a=int(x)-(mean(newData))
    a**=2
    squareList.append(a)

sum=0
for i in squareList:
    sum+=i

result=sum/(len(newData)-1)
sd=math.sqrt(result)
print(sd)
