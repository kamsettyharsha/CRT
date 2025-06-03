def count_frequencies(arr):
    freq={}
    for num in arr:
        freq[num]=freq.get(num,0)+1
print(freq) 
maxi=max(freq,key=freq.get) 
print(maxi)    