# -*- coding: utf-8 -*-

import numpy as npy
import random
import sympy as sp
from numpy.linalg import matrix_rank
npy.set_printoptions(threshold=npy.inf)
from pyfinite import ffield


string_to_hexa = {'f' : [0,0,0,0],
 'g' : [0,0,0,1],
 'h' : [0,0,1,0],
 'i' : [0,0,1,1],
 'j' : [0,1,0,0],
 'k' : [0,1,0,1],
 'l' : [0,1,1,0],
 'm' : [0,1,1,1],
 'n' : [1,0,0,0],
 'o' : [1,0,0,1],
 'p' : [1,0,1,0],
 'q' : [1,0,1,1],
 'r' : [1,1,0,0],
 's' : [1,1,0,1],
 't' : [1,1,1,0],
 'u' : [1,1,1,1]}

hexa_to_string = {'0000': 'f',
 '0001': 'g',
 '0010': 'h',
 '0011': 'i',
 '0100': 'j',
 '0101': 'k',
 '0110': 'l',
 '0111': 'm',
 '1000': 'n',
 '1001': 'o',
 '1010': 'p',
 '1011': 'q',
 '1100': 'r',
 '1101': 's',
 '1110': 't',
 '1111': 'u'}


#It maps set of two charachters(byte) to it's corresponding hex value
def map_to_asc(str):
    char = chr(16*(ord(str[0]) - ord('f')) + ord(str[1]) - ord('f'))
    return char
#It takes a full block of ip eg 'ffgfffffffffffff' and outputs corresponding hexa list
def block_to_asc(ch):
    plaintext = ""
    for i in range(0, len(ch), 2):
        plaintext += map_to_asc(ch[i:i+2])
    return plaintext
#It converts byte to corresponding two charachters
def byte_string(b):
    binary_number = '{:0>8}'.format(format(b,"b"))
    a = hexa_to_string[binary_number[0:4]], hexa_to_string[binary_number[4:8]]
    return a[0]+a[1]

#It contains all the required functions for reuse
#Add, multiplication,Expo, vectoraddition, multiplicationscalars, LinearTransformation
storepower = [[-1]*128 for i in range(128)]

F = ffield.FField(7)

def Add (num1, num2):
    return int(num1) ^ int(num2)

def multiplication (num1, num2):
    return F.Multiply(num1, num2)

def Expo (num, pow):
    if storepower[num][pow] != -1:
        return storepower[num][pow]

    result = 0;
    if pow == 0:
        result = 1
    elif pow == 1:
        result = num
    elif pow%2 == 0:
        sqrt_no = Expo(num, pow>>1)
        result = multiplication(sqrt_no, sqrt_no)
    else:
        sqrt_no = Expo(num, pow>>1)
        result = multiplication(sqrt_no, sqrt_no)
        result = multiplication(num, result)

    storepower[num][pow] = result
    return result

def vectoraddition (v1, v2):
    result = [0]*8
    for i, (e1, e2) in enumerate(zip(v1, v2)):
        result[i] = Add(e1, e2)
    return result

def multiplicationscalars (v, elem):
    result = [0]*8
    for i, e in enumerate(v):
        result[i] = multiplication(e, elem)
    return result

def LinearTransformation (mat, elist):
    result = [0]*8
    for row, elem in zip(mat, elist):
        result = vectoraddition(multiplicationscalars(row, elem), result)
    return result

#This list will consist of all possible exponents
expvalues = [[] for i in range(8)]
#This list will consist of all possible diagonal values
diag_poss_val = [[[] for i in range(8)] for j in range(8)]
input_file = open("inputs.txt", 'r')
output_file = open("outputs.txt", 'r')
for ind, (iline, oline) in enumerate(zip(input_file.readlines(), output_file.readlines())):
    inputstring = []
    outputstring = []
    #Converting each input to corresponding hex values
    for hexi in iline.strip().split(" "):
        inputstring.append(block_to_asc(hexi)[ind])
    for hexo in oline.strip().split(" "):
        outputstring.append(block_to_asc(hexo)[ind])
        
    for i in range(1, 127):
        for j in range(1, 128):
            flag = True
            for inp, out in zip(inputstring, outputstring):
                if ord(out) != Expo(multiplication(Expo(multiplication(Expo(ord(inp), i), j), i), j), i):
                    flag = False
                    break
            if flag:
                expvalues[ind].append(i)
                diag_poss_val[ind][ind].append(j)
# Printing each row in a different line
print("The Linear Transformation Matrix with Possible Values of Diagonal Elements is : \n")
length = len(diag_poss_val)
first_row=diag_poss_val[:(9 - length)]
print(first_row)
second_row=diag_poss_val[(9 - length):(10 - length)]
print(second_row)
third_row=diag_poss_val[(10 - length):(11 - length)]
print(third_row)
fourth_row=diag_poss_val[(11 - length):(12 - length)]
print(fourth_row)
fifth_row=diag_poss_val[(12 - length):(13 - length)]
print(fifth_row)
sixth_row=diag_poss_val[(13 - length):(14 - length)]
print(sixth_row)
seventh_row=diag_poss_val[(14 - length):(15 - length)]
print(seventh_row)
eigth_row=diag_poss_val[(15 - length):(16 - length)]
print(eigth_row)
print("\n")
print("The Exponent Vector Matrix with Possible Values of all the Elements is : \n")
print(expvalues)
print("\n") 

input_file = open("inputs.txt", 'r')
output_file = open("outputs.txt", 'r')
for ind, (iline, oline) in enumerate(zip(input_file.readlines(), output_file.readlines())):
    #Considering only first 6 pairs
    if ind > 6 :
        break
    inputstring = []
    outputstring = []
    #Converting each input to corresponding hexa values
    for hexi in iline.strip().split(" "):
        inputstring.append(block_to_asc(hexi)[ind]) 
    for hexo in oline.strip().split(" "):
        outputstring.append(block_to_asc(hexo)[ind+1])
    for i in range(1, 128):
        for p1, e1 in zip(expvalues[ind+1], diag_poss_val[ind+1][ind+1]):
            for p2, e2 in zip(expvalues[ind], diag_poss_val[ind][ind]):
                flag = True
                for input, output in zip(inputstring, outputstring):
                    if ord(output) != Expo(Add(multiplication(Expo(multiplication(Expo(ord(input), p2), e2), p2), i) ,multiplication(Expo(multiplication(Expo(ord(input), p2), i), p1), e1)), p1):
                        flag = False
                        break
                if flag:     
                    expvalues[ind+1] = [p1]
                    diag_poss_val[ind+1][ind+1] = [e1]
                    expvalues[ind] = [p2]
                    diag_poss_val[ind][ind] = [e2]
                    diag_poss_val[ind][ind+1] = [i]
length = len(diag_poss_val)
# Printing each row in a different line
print("The Linear Transformation Matrix with Elements just next to Diagonal ELements is : \n")
first_row=diag_poss_val[:(9 - length)]
print(first_row)
second_row=diag_poss_val[(9 - length):(10 - length)]
print(second_row)
third_row=diag_poss_val[(10 - length):(11 - length)]
print(third_row)
fourth_row=diag_poss_val[(11 - length):(12 - length)]
print(fourth_row)
fifth_row=diag_poss_val[(12 - length):(13 - length)]
print(fifth_row)
sixth_row=diag_poss_val[(13 - length):(14 - length)]
print(sixth_row)
seventh_row=diag_poss_val[(14 - length):(15 - length)]
print(seventh_row)
eigth_row=diag_poss_val[(15 - length):(16 - length)]
print(eigth_row)
print("\n")
print("The Exponent Vector Matrix with all the Elements is : \n")
print(expvalues)
print("\n")
#Function used to apply operations (EAEAE)
def EAEAE (plaintext, linearmatrix, expomatrix):
    plaintext = [ord(ch) for ch in plaintext]
    output = [[0 for j in range (8)] for i in range(8)]
    for ind, elem in enumerate(plaintext):
        output[0][ind] = Expo(elem, expomatrix[ind])

    output[1] = LinearTransformation(linearmatrix, output[0])

    for ind, elem in enumerate(output[1]):
        output[2][ind] = Expo(elem, expomatrix[ind])

    output[3] = LinearTransformation(linearmatrix, output[2])

    for ind, elem in enumerate(output[3]):
        output[4][ind] = Expo(elem, expomatrix[ind])
    return output[4]
for index in range(6):
    #As we have already found the element just after the diagonal, we skip two elements every time
    of = index + 2
    
    exponentmatrix = [e[0] for e in expvalues]
    lineartransformationmatrix = [[0 for i in range(8)] for j in range(8)]
    #We fill all the empty [] elements with 0
    for i in range(8):
        for j in range(8):
            lineartransformationmatrix[i][j] = 0 if len(diag_poss_val[i][j]) == 0 else diag_poss_val[i][j][0]
    input = open("inputs.txt", 'r')
    out = open("outputs.txt", 'r')
    for ind, (iline, oline) in enumerate(zip(input.readlines(), out.readlines())):
        if ind > (7-of):
            continue
        inputstring = [block_to_asc(msg) for msg in iline.strip().split(" ")]
        outputstring = [block_to_asc(msg) for msg in oline.strip().split(" ")]
        #We find for which values of a_(i,j) EAEAE = Output is satisfied 
        for i in range(1, 128):
            lineartransformationmatrix[ind][ind+of] = i
            flag = True
            for inp, out in zip(inputstring, outputstring):
                if EAEAE(inp, lineartransformationmatrix, exponentmatrix)[ind+of] != ord(out[ind+of]):
                    flag = False
                    break
            if flag:
                diag_poss_val[ind][ind+of] = [i]
    input.close();
    #out.close();


lineartransformationmatrix = [[0 for i in range(8)] for j in range(8)]
for i in range(8):
    for j in range(8):
        lineartransformationmatrix[i][j] = 0 if len(diag_poss_val[i][j]) == 0 else diag_poss_val[i][j][0]


# Printing each row of the final matrix in a different line
print("The Final Linear Transformation Matrix is : \n")
length = len(lineartransformationmatrix)
first_row=lineartransformationmatrix[:(9 - length)]
print(first_row)
second_row=lineartransformationmatrix[(9 - length):(10 - length)]
print(second_row)
third_row=lineartransformationmatrix[(10 - length):(11 - length)]
print(third_row)
fourth_row=lineartransformationmatrix[(11 - length):(12 - length)]
print(fourth_row)
fifth_row=lineartransformationmatrix[(12 - length):(13 - length)]
print(fifth_row)
sixth_row=lineartransformationmatrix[(13 - length):(14 - length)]
print(sixth_row)
seventh_row=lineartransformationmatrix[(14 - length):(15 - length)]
print(seventh_row)
eigth_row=lineartransformationmatrix[(15 - length):(16 - length)]
print(eigth_row)
print("\n")

print("The Final Exponent Vector Matrix is : \n")
print(exponentmatrix)
print("\n")

#Two halves of the password
password_1 = "lhlrmfjffiitflmi"
password_2 = "jtlimshtmhfrfqkk"

#We find for which input the password halves match
def decrypt(password):
    password_ = block_to_asc(password)
    res = ""
    for ind in range(8):
        for ans in range(128):
            input = res + byte_string(ans)+(16-len(res)-2)*'f'
            if ord(password_[ind]) == EAEAE(block_to_asc(input),lineartransformationmatrix, exponentmatrix)[ind]:
                res += byte_string(ans)
                break
    return res
decrypt_pass = block_to_asc(decrypt(password_1))+block_to_asc(decrypt(password_2)) 

print("Decrypted Password with Padding is : ",block_to_asc(decrypt(password_1))+block_to_asc(decrypt(password_2)))
print("\n")
final_pass = decrypt_pass[:-6]
print("Final Password is : ",final_pass)     

