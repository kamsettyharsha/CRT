arr=[1,2,5,4,3]
N=len(arr)
arr.sort()
sum=0
A=arr[-1]
B=arr[-2]
Avg=(A+B)/2
for i in range(N):
    if(arr[i]<Avg):
        arr[i]=0
for i in range(N):        
        sum=sum+arr[i]
print(sum)
      
    

