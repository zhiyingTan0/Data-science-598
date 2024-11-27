import pandas as pd

def nonDictionary(df_new,wordList):
    namesDict={"Twilight Sparkle":"twilight","Applejack":"applejack","Rarity":"rarity","Pinkie Pie":"pinkie","Rainbow Dash":"rainbow","Fluttershy":"fluttershy"}
    nonDict={}
    for name in namesDict:
        dfPony = df_new.loc[df_new['pony']==name] 
        dfPony['dialog']=dfPony['dialog'].replace('<U\+.*>'," ", regex = True)
        dfPony['dialog']=dfPony['dialog'].replace('[^A-Za-z0-9]'," ",regex=True)
        dict={}
        for dialog in dfPony.dialog:
            dialogList=dialog.split(" ")
            for i in dialogList:
                if i=='':
                    continue
                if i.lower() in dict:
                    dict[i.lower()]=dict[i.lower()]+1
                else:
                    dict[i.lower()]=1
        #print(dict)
        acc=[]
        #print("I".lower() in wordList)
        while len(acc)<5 and ((not dict)==False):
            max_value = max(dict.values())
            max_keys = [k for k, v in dict.items() if v == max_value]
            for i in max_keys:
                if i.lower() in wordList:
                    dict.pop(i)
                else:
                    acc.append(i)
                    dict.pop(i)
        nonDict[namesDict[name]]=acc
    return nonDict