def Quick(arr):
    if len(arr)<=1:
        return arr
    left=[]
    right=[]
    equal=[]
    pvt=arr[-1]
    for i in arr:
        if(i<pvt):
            left.append(i)
        elif (i>pvt):
            right.append(i)
        else:
            equal.append(i)
    print("pivot:",pvt)  
    print("left sub array",left)
    print("right sub array",right)
    print("equal sub array",equal) 
    return Quick(left)+equal+Quick(right)   
arr=[23,63,44,57,12,45,36] 
print(Quick(arr))                    

