from itertools import zip_longest
l1=[i for i in range(10)]
l2=[i for i in range(7)]
print(l1,'\n',l2)
out=[]
k=0
for i,j in zip_longest(l1,l2,fillvalue=''):
    k=i+j
out.append(k)
print(out)