l=[]
n=int(input("num ele:"))
for i in range(n):
    e=int(input(f"pleas enter the element at index {i}:"))
    l.append(e)
l.sort()
print(f"the list is {l}")

t=int(input("enter the target:"))
while len(l):
    for i in l:
        j=i+1
        for j in l:
            if t==i+j:
                print(f"target found.{i}+{j}={t}")
            else:
                pass
    break
            