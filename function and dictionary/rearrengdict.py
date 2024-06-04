d={
    "agent name":["Sova","Jett","Comber","Brimstone","Reyna"],
    "agent type":["Initiator","Duelist","Sentinel","Controlar","Duelist"],
    "Sequence":[1,3,5,2,4]
}
newdict={}
corellation=[]

for i in range(0,len(d["agent name"])):#This is how we access values from dictionary
    corellation.append((d["agent name"][i],d["agent type"][i]))

print(corellation)

for serial in range(1,max(d["Sequence"])+1):
    position=d["Sequence"].index(serial) #we collect index number of sequence
    newdict[serial]=corellation[position]

print(newdict)
#class 23 done