#LEFT ROTATION
def rotateArr(self, arr, d):
        #Your code here
        n=len(arr)
        temp=[0]*n
        d=d%n
        for i in range(len(arr)):
            arr[i]=temp[(n-d+i)%n]
        for i in range(len(arr)):
            temp[i]=arr[i]
        return arr    

#RIGHT ROTATION
def rotateArr(self, arr, d):
    n=len(arr)
    temp=[0]*n
    d=d%n
    for i in range(len(arr)):
        temp[(d+i)%n]=arr[i]
    for i in range(len(arr)):
        arr[i]=temp[i]
    return arr        