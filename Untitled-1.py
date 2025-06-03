class Solution:
    def frequencyCount(self, arr):
        freq={}
        ans=[]
        n=len(arr)
        for i in arr:
            freq[i]=freq.get(i,0)+1
        for i in range(1,n+1):
            ans.append(freq.get(i,0))
        return (max,min(ans))      