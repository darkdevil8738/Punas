from itertools import zip_longest
w1=input("word1=")
w2=input("word2=")
k=[]
for i,j in zip_longest(w1,w2,fillvalue=''):
    k.append(i+j)
print("".join(k))
print()