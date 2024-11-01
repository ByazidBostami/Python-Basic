print(type(10))
print(type("Byazid"))
print(type(10.5))
print(type(True))
s="My Name is Byazid"
s1=s.lower()
s2=s.upper()
name="byazid bostami"
capName=name.capitalize()
titlename=name.title()
print(s1,s2,capName,titlename)
print(dir(s))
print(id(s))
items=[1,2,23,"abc",4,32,"IlvoeYou"]

print("x" in items)
print("abc" in items)
for item in items:
    print(item)

ustr="dhaka"
ustr2=['d', 'h', 'a', 'k', 'a']
for i in ustr:
    print(list(i))

print(list(ustr))
ustr2[0]="D"
s2="".join(ustr2) #list to string
print(s2)