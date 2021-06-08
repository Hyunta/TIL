li = ["c=","c-","dz=","d-","lj","nj","s=","z="]
s = input()

for t in li:
    s = s.replace(t,'a')
print(len(s))