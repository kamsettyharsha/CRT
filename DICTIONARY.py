def count_frequencies(arr):
    freq={}
    for num in arr:
        freq[num]=freq.get(num,0)+1
        return freq
arr=[1,2,3,4,4,3,2,1,1,1,2,2,3,3,4,4]    
frequencies=count_frequencies(arr)  
for i, count in frequencies.items():
    print(i,count)



class Solution:
    def findFrequency(self, arr, x):
        # code here
        d={}
        for i in arr:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        ans=d.get(x)
        if(ans!=None):
            return ans
        elif(ans==None):
            return 0
class Solution:
    # Function to count the frequency of all elements from 1 to N in the array.
    def frequencyCount(self, arr):
        #  code here
        freq={}
        ans=[]
        n=len(arr)
        for i in arr:
            freq[i]=freq.get(i,0)+1
        for i in range(1,n+1):
            ans.append(freq.get(i,0))
        return ans    
        
    

arr=[1,2,3,4,5,5]
freq={}
for num in arr:
    freq[num]=freq.get(num,0)+1
print(freq) 
maxi=max(freq,key=freq.get) 
mini=min(freq,key=freq.get)
print(maxi)   
print(mini)
print("maximum frequency number:",maxi)
print("m frequency number:",mini)


            
            
        


















