#Known RSA parameters
e = 5
N=84364443735725034864402554533826279174703893439763343343863260342756678609216895093779263028809246505955647572176682669445270008816481771701417554768871285020442403001649254405058303439906229201909599348669565697534331652019516409514800265887388539283381053937433496994442146419682027649079704982600857517093
C=521734975285013699424664163387815953077899955174226167820584409005930365154978006363366478210384084219813332819148632301755076155629591431637130380855574208554795904340660497175038871108978115944604825883131981199326682705978802830581435144945719777738234956026563438426236821114790314941118510178357999248
#Breaking RSA 
str_p = "The_Kryptonians: This door has RSA encryption with exponent 5 and the password is "
bin_str_p = ''.join(['{0:08b}'.format(ord(p)) for p in str_p])
mod_N = Zmod(N)
m_max_len = 250
eps = 1/7
flag =1
for m_len in range(0, m_max_len+1, 4):
    P.<m> = mod_N[]
    poly = ((int(bin_str_p,2)<<m_len)+m)^e-C
    deg = poly.degree()
    mm = ceil(1/(deg*eps))
    pp = ceil(N**((1/deg)-eps))

    n= deg*mm
    poly_Z = poly.change_ring(ZZ)
    P = poly_Z.parent().gen()
    
    #Computing Polynomials
    poly_f = []
    for i in range(n):
        for j in range(deg):
            poly_f.append((P * pp)**j * poly_Z(P * pp)**i * N**(mm - i))

    #Constructing Lattice Lat
    Lat = Matrix(ZZ, n)
    for i in range(n):
        for j in range(i+1):
            Lat[i, j] = poly_f[i][j]
    Lat = Lat.LLL()

    # Transforming shortest vector in polynomial
    new_poly = 0
    for i in range(n):
        new_poly += (P**i * Lat[0, i])/(pp**i)

    #Factoring polynomial
    possible_roots = new_poly.roots()

    # testing possible roots
    final_roots = []
    for root in possible_roots:
        if root[0].is_integer():
            ans = poly_Z(ZZ(root[0]))
            if gcd(N,ans) >= N:
                final_roots += [ZZ(root[0])]

    if final_roots : 
        bin_pass = '{0:b}'.format(final_roots[0])
        extra_zeroes = 8-len(bin_pass)%8   #adding zeroes to bin_pass from left side to make length of bin_pass a multiple of 8    
        bin_pass =  '0'*extra_zeroes + bin_pass
        print("Binary Password: ",bin_pass)

        password = ''
        for bin_ in range(0,len(bin_pass),8):
            password += chr(int(bin_pass[bin_:bin_+8],2))

        print("Password: '{}'".format(password))
        flag=0

if flag: 
    print("No Solution")


