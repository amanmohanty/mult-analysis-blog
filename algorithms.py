import numpy as np

def quadratic(num1, num2):
    """
    Quadratic algorithm
    """

    if len(num1) == 0 or len(num2) == 0: 
        return "0"
    res = [0] * (len(num1) + len(num2)) 
    ind_n1 = 0
  
    for i in range(len(num1) - 1, -1, -1): 
        c = 0
        n1 = ord(num1[i]) - 48
        ind_n2 = 0
  
        for j in range(len(num2) - 1, -1, -1): 
            n2 = ord(num2[j]) - 48
            prod = n1*n2 + res[ind_n1+ind_n2] + c 
            c = prod // 10
            res[ind_n1+ind_n2] = prod % 10
            ind_n2 += 1
  
        res[ind_n1+ind_n2] += c
        ind_n1 += 1

    i = len(res) - 1
    while (i >= 0 and res[i] == 0): 
        i -= 1
    if (i == -1): 
        return "0"

    s = ""

    while (i >= 0): 
        s += chr(res[i] + 48) 
        i -= 1
  
    return s 

def fft(num1,num2):
    """
    FFT algorithm
    """
    N = len(num1)
    arr_a1=np.pad(num1,(0,N),'constant')
    arr_b1=np.pad(num2,(0,N),'constant')
    a_f=np.fft.fft(arr_a1)
    b_f=np.fft.fft(arr_b1)

    c_f=[0]*(2*N)

    for i in range( len(a_f) ):
        c_f[i]=a_f[i]*b_f[i]

    return np.fft.ifft(c_f)

def karat(x,y):
    """
    Karatsuba algorithm
    """

    num1 = int(x)
    num2 = int(y)
    if len(x) == 1 or len(y) == 1:
        return num1*num2
    else:
        m = max(len(x),len(y))
        m2 = m // 2

        a = num1 // 10**(m2)
        b = num1 % 10**(m2)
        c = num2 // 10**(m2)
        d = num2 % 10**(m2)

        z0 = karat(str(b),str(d))
        z1 = karat(str(a+b),str(c+d))
        z2 = karat(str(a),str(c))

        return str( (int(z2) * 10**(2*m2)) + ((int(z1) - int(z2) - int(z0)) * 10**(m2)) + int(z0) )

def python(x,y):
    """
    Python internal multiplication
    """
    return int(x)*int(y)