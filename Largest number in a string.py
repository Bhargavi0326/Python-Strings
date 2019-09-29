S=input().split(".")
M=S[0]
P=[]
Li=M.split()
for i in Li:
    if i.isdigit():
        P.append(int(i))
print(max(P))
