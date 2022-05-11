def Coeff_e(p,n):
    e=[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for i in range(1,32):
        sum=0
        for j in range(1,i+1):
            sum+= ((e[i-j]*p[j])%n *((-1)**(j-1)))
            sum=sum%n
        e[i]=sum%n
        for s in range(n):
            if (s*i)%n ==e[i]:
                e[i]=s
                break
    return e

def Poly_roots(e,p):
    roots=[]
    for i in range(127):
        sum=0
        for j in range(p[0]+1):
            sum += (i**(p[0]-j)%127*e[j])%127 *((-1)**j)   
            sum=sum%127
        if(sum==0):
            roots.append(i)
            Total_roots.append(i)
    return roots

def reduced_powersum(roots,p):
    new_p=[p[0]-len(roots)]
    for i in range(1,32):
        sum=0
        for j in range(len(roots)):
            sum+= (roots[j]**i)%127
            sum=sum%127
        new_p.append((p[i]-sum)%127) 
    return new_p     
           

p = [ 22, 11, 7, 93, 125, 27, 46, 65, 24, 92, 93, 27, 65, 59, 101, 22 ,104 ,78, 59, 5, 90, 16, 101, 80, 9 ,81, 97, 108, 65, 100, 87, 40
]
m=p[0]
n = 127
Total_roots=[]
for i in range(32):
    e=Coeff_e(p,n)
    roots=Poly_roots(e,p)
    print(roots)
    p=reduced_powersum(roots,p)
    
    if len(Total_roots)==m:
        break

Total_roots.sort()
password=""  
for i in range(len(Total_roots)):
    password+=chr(Total_roots[i])

print("Password is:",password)    
