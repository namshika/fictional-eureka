print("Welcome to maths question paper generator for class 10")
a=int(input("\nSelect maximum number of marks: "))
s=1
print("\nPatterns possible\n")
print("S.no | 2 mark | 3 mark | 5 mark")
for i in range(1,a//2):
    for j in range(1,a//2):
        for k in range(1,a//2):
            if ((2*i)+(3*j)+(5*k)==a):
                print(s,". \t ",i," \t ",j," \t ",k)
                s=s+1                      
x=int(input("\nSelect the serial number for the pattern of the question paper: "))

s=1
flag=0
for i in range(1,a//2):
    for j in range(1,a//2):
        for k in range(1,a//2):
            if ((2*i)+(3*j)+(5*k)==a):
                if (s==x):
                  flag=1
                s=s+1  
            if(flag==1):
                break
        if(flag==1):
            break
    if(flag==1):
        break


print("The number of questions for each section are:\n2 mark: ",i,"\n3 mark:",j,"\n5 mark: ",k)

#getting 2 mark qns in list
import random
fp=open("2mark.txt","r")
c=[]
b=fp.readlines()
y=len(b)-1
for n in range(i):   
    m=random.randint(0,y)
    a1=b[m]
    if a1 not in c:
        c.append(a1)
fp.close()

#getting 3 mark qns in list
fp1=open("3mark.txt","r")
e=fp1.readlines()
z=len(e)-1
for n in range(j): 
    m=random.randint(0,z)
    a2=e[m]
    if a2 not in c:
        c.append(e[m])
fp1.close()

#getting 5 mark qns in list
fp2=open("5mark.txt","r")
l=fp2.readlines()
s=len(l)-1
for i in range(k):
    m=random.randint(0,s)
    a3=l[m]
    if a3 not in c:
        c.append(a3)
fp2.close()
#print(c)
fp3=open("final.txt","w")
fp3.writelines(c)
fp3.close()

print("\nQuestion paper successfully generated! Open final.txt to access it!\n")