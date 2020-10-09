import pandas as pd

def followOnComments(df):
    #names=["Twilight Sparkle","Applejack","Rarity","Pinkie Pie","Rainbow Dash","Fluttershy","Others"]
    followDict={}
    namesDict={"Twilight Sparkle":"twilight","Applejack":"applejack","Rarity":"rarity","Pinkie Pie":"pinkie","Rainbow Dash":"rainbow","Fluttershy":"fluttershy","Others":"other"}
    for name in namesDict:
        names=["Twilight Sparkle","Applejack","Rarity","Pinkie Pie","Rainbow Dash","Fluttershy","Others"]
        names.remove(name)
        acc=[0,0,0,0,0,0]
        listPony = [pony for pony in df.pony]
        listTitle=[title for title in df.title]
        for i in range(1,len(listPony)):
            if listPony[i]!=name or listTitle[i]!=listTitle[i-1]:
                continue
            others=1
            for j in range (5):
                if listPony[i-1]==names[j]:
                    acc[j]=acc[j]+1
                    others=0
                    break
            if others==1:
                 acc[5]=acc[5]+1
        if sum(acc)==0:
            followDict[namesDict[name]]={ namesDict[names[i]]: str(round(0,2) )for i in range(len(acc))}
        else:
            followDict[namesDict[name]]={ namesDict[names[i]]: str(round(acc[i]/sum(acc),2) )for i in range(len(acc))}      
       
        #followDict[namesDict[name]]={ namesDict[names[i]]: str(round(acc[i]/sum(acc),2) )for i in range(len(acc))}
    followDict.pop("other")           
    return followDict  
