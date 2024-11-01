dic1 = {'Harry':15, 'Draco':8, 'Nevil':19}
dic2 = {'Ginie':18, 'Luna': 14}

check = dic1.copy()
check.update(dic2)

print (check)

#another method 
# check = {**dic1,**dic2}