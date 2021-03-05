import gmpy2
from Crypto.Util.number import *
from flag import flag
from pubkey.pem import n,e

def get_N(i):
     p=getPrime(i)
     q=nextprime(p)
     n=p**2*q
     return n

m=bytes_to_long(flag)
c=pow(m,e,get_N(520))

cipher=base64.base64encode(long_to_bytes(c))

with open("flag.enc","w") as f:
    f.write(cipher)
    f.close




