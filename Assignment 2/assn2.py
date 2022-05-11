import numpy as np

keyword=input("enter keyword:")
keyword=keyword.lower()

ciphertext=input("Enter ciphertext:")
ciphertext=ciphertext.lower()
ciphertext=ciphertext.replace("j","i")
ciphertext=list(ciphertext)

st=list()

for i in ciphertext:
    if i.isalpha():
        s.append(i)

l=len(st)

if(l%2!=0):
    st.append("z")
    l+=1


b=list()
e=list()

for i in range(97,123):
    if(chr(i)!="j"):
        e.append(chr(i))

m=0
n=0
d={}
for i in range(5):
    c=[]
    while(len(c)!=5):
        if(n!=len(keyword)):
            if keyword[n] not in d:
                c.append(keyword[n])
                d[keyword[n]]=1
            n+=1
        else:
            if e[m] not in d:
                c.append(e[m])
                d[e[m]]=1
            m+=1

    b.append(c)

key=np.array(t)

r=np.where(key=="r")

pt=[]

for i in range(0,le,2):
    r1=np.argwhere(key==s[i])
    r2=np.argwhere(key==s[i+1])
    
    if(r1[0][1] == r2[0][1]):
        if(r1[0][0]!=0):
            pt.append(key[r1[0][0]-1][r1[0][1]])
        elif(r1[0][0]==0):
            pt.append(key[4][r1[0][1]])

        if(r2[0][0]!=0):
            pt.append(key[r2[0][0]-1][r2[0][1]])
        elif(r2[0][0]==0):
            pt.append(key[4][r2[0][1]])
    elif(r1[0][0]==r2[0][0]):
        if(r1[0][1]!=0):
            pt.append(key[r1[0][0]][r1[0][1]-1])
        elif(r1[0][1]==0):
            pt.append(key[r1[0][0]][4])
        if(r2[0][1]!=0):
            pt.append(key[r2[0][0]][r2[0][1]-1])
        elif(r2[0][1]==0):
            pt.append(key[r2[0][0]][4])

    else:
        pt.append(key[r1[0][0]][r2[0][1]])
        pt.append(key[r2[0][0]][r1[0][1]])

plaintext=str()
for i in range(len(res)):
    plaintext+=pt[i]
    
print()
print(plaintext)