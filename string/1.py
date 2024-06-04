#a
for i in range(24,-7,-6):
    if i==-6:
        print(i,end='#')
    else:
        print(i,end=',')
#b
for j in range(-10,21,5):
    if j==20:
        print(j,end='#')
    else:
        print(j,end=",")
#c
for k in range(18,64,9):
    if k==63:
        print(k,end="#")
    else:
        print(k,end=",")
#d
for l in range(18,64,9):
    if l<64:
        if l%2==0:
            print(l,end=",")
        else:
            if l==63:
                print(l*-1,end="")
            else:
                print(l*-1,end=",")