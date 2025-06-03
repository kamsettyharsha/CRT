arr=list(map(int,input().split()))
R=int(input())
U=int(input())
N=int(input())
Food_Required=R*U
if(Food_Required==0):
    print(-1)
for i in range(N):
    Food_Required=Food_Required-arr[i]
    if (Food_Required<0):
        break
print(abs(Food_Required))    
