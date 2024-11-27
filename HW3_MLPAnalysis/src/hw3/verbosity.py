import pandas as pd
import math

def gen_verbosity(df):
    # twilight, applejack, rarity, pinkie, raibow, fluttershy
    size=len(df)
    verbosity={}
    acc=[0.0 for i in range(6)]
    for i in range(size):
        #print(i," ",df.pony[i]=="Twilight Sparkle")
        if(df.pony[i]=="Twilight Sparkle"):acc[0]=acc[0]+1
        elif(df.pony[i]=="Applejack"):acc[1]=acc[1]+1
        elif(df.pony[i]=="Rarity"):acc[2]=acc[2]+1
        elif(df.pony[i]=="Pinkie Pie"):acc[3]=acc[3]+1
        elif(df.pony[i]=="Rainbow Dash"):acc[4]=acc[4]+1
        elif(df.pony[i]=="Fluttershy"):acc[5]=acc[5]+1
    acc=[i/sum(acc) for i in acc]
    verbosity["twilight"]=str(round(acc[0],2))
    verbosity["applejack"]=str(round(acc[1],2))
    verbosity["rarity"]=str(round(acc[2],2))
    verbosity["pinkie"]=str(round(acc[3],2))
    verbosity["rainbow"]=str(round(acc[4],2))
    verbosity["fluttershy"]=str(round(acc[5],2))

    return verbosity