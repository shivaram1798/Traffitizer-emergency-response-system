# Enter your code here. Read input from STDIN. Print output to STDOUT
string1=input()
inputt=[]
for i in string1:
    inputt.append(i)
result=[]
result.append(inputt)
temp=[]
for i in inputt:
    temp.append(i)

for i in range(len(temp)-1):
    for j in range(i+1,len(temp)):
        temp[i],temp[j]=temp[j],temp[i]
        result.append(temp)
        for k in inputt:
            temp.append(k)

print(result)
