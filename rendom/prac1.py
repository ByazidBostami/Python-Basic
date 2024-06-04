
python_student=[]
final_list=[]
max_score=0
max2=0
for i in range(int(input())):
    name = input()
    score = float(input())
    python_student+=[name,score]
    
for i in range(0,len(python_student),2):
    final_list.append([python_student[i],python_student[i+1]])


print(final_list)