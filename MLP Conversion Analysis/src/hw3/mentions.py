import pandas as pd

def wordString(dialog,word):
    acc=0
    s=" "+dialog+" "
    #print(s)
    for i in range(1,(len(dialog)+1-len(word)+1)):
        #print(i,":",s[i:i+len(word)])
        if s[i:i+len(word)]==word and s[i-1].isalnum()==False and s[i+len(word)].isalnum()==False:
            acc=acc+1
    return acc
    
def wordMention(df,name):
    nameSplit=name.split()
    acc=0
    if len(nameSplit)==1:
        for dialog in df.dialog:
            acc=acc+wordString(dialog,name)
    else:
        for dialog in df.dialog:
            acc=acc+wordString(dialog,nameSplit[0])+wordString(dialog,nameSplit[1])-wordString(dialog,name)
    return acc

def gen_mentions(df_new):
    mentionsOut={}
    names1=["Twilight Sparkle","Applejack","Rarity","Pinkie Pie","Rainbow Dash","Fluttershy"]
    for name in names1:
        names=["Twilight Sparkle","Applejack","Rarity","Pinkie Pie","Rainbow Dash","Fluttershy"]
        namesDict={"Twilight Sparkle":"twilight","Applejack":"applejack","Rarity":"rarity","Pinkie Pie":"pinkie","Rainbow Dash":"rainbow","Fluttershy":"fluttershy"}
        abc=names.remove(name)
        acc=[]
        #return wordMention(df_new.loc[df_new.pony==name],"Twilight Sparkle")
        if len(df_new.loc[df_new.pony==name])==0:
            mentionsOut[namesDict[name]]={namesDict[names[i] ]: str(round(0,2) )for i in range(len(names))}
            continue
        for pony1 in names:

            count=wordMention(df_new.loc[df_new.pony==name],pony1)
            acc.append(count)
        if sum(acc)==0:
            mentionsOut[namesDict[name]]={namesDict[names[i] ]: str(round(0,2) )for i in range(len(names))}
            continue
        #return [names[i]+":"+str(acc[i]/sum(acc) )for i in range(len(acc))]
        else:
            mentionsOut[namesDict[name]]={namesDict[names[i] ]: str(round(acc[i]/sum(acc),2) )for i in range(len(acc))}
    return mentionsOut