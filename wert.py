n = int(input())
string = input()
lis=[]
list1 = list(string.split(" "))
for i in range(n):
    lis.append(int(list1[i]))
lis.sort(reverse = True)
count=0
x=lis[0]-lis[3]
while x!=0:
    if x >=5:
        su=5
    elif x>=2:
        su=2
    else:
        su=1
    for i in range(1,n):
        z=lis[i]+su
        lis[i]=z
    lis.sort(reverse = True)
    count=count+1
    su=0
    x=lis[0]-lis[3] 
print(count)

