re=[]
n=6
for i in range(6):
    cur=[1]
    re.append(cur)
    if i == 0:
        continue
    for j in range(len(re[i-1])-1):
        cur.append(re[i-1][j] + re[i-1][j+1])
    cur.append(1)
print(re)

re=[[1],[1,1]]
n=6
for i in range(2,6):
    row=[1]
    for j in range(i-1):
        row.append(re[i-1][j]+re[i-1][j+1])
    row.append(1)
    re.append(row)
print(re)

n=6
oldline=[]
newline=[1]
ww=[]
print(newline)
for i in range(1,n):
    oldline=newline.copy()
    oldline.append(0)
    newline.clear()
    for j in range(i+1):
        newline.append(oldline[j-1] + oldline[j])
        if j==(i)//2:
            ww=newline.copy()
            newline.sort(reverse=True)
            if i%2==0:
                del ww[-1]
                for k in newline:
                    ww.append(k)
            print(ww)


