d={
    "agent name":["Sova","Jett","Comber","Brimstone","Reyna"],
    "agent type":["Initiator","Duelist","Sentinel","Controlar","Duelist"],
    "Sequence":[1,3,5,2,4]
}

mydict={}
controlar=[]

for i in range(0,len(d["agent name"])):
    controlar.append((d["agent name"][i],d["agent type"][i]))

print(controlar)
for position in range(1,max(d["Sequence"])):
    pos=d["Sequence"].index(position)
    mydict[position]=controlar[pos]

print(mydict)