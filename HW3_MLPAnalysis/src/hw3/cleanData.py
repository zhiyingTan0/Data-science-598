import pandas as pd

def cleanData (df):
    i=1
    ptr=0
    size=len(df)
    while (i<size):
        if (df.title[i]==df.title[ptr]) and (df.pony[i]==df.pony[ptr]):
            df.loc[ptr]['dialog']=df.loc[ptr]['dialog']+" "+df.loc[i]['dialog']
            df.drop(index=i,inplace=True)
            i=i+1
        else:
            ptr=i
            i=i+1


