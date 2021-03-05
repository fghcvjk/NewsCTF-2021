import gmpy2
import sympy
from Crypto.Util.number import *
from flag import flag


z=getPrime(1024)
p=sympy.nextprime(z)
q=sympy.prevprime(10*z)
n=p*q

m=bytes_to_long(flag)
e=0xe18e
c=pow(m,e,n)
print(c)


#n=0x2c404d87c6244ad1b44aabd95244d5deb3c93cf3bd798ba4624cd9f89c95e246aad9cbda463292c6ef3140d97c5c1e691c54095e75f56d61a1640decc83caccce52c957282949bed20105d4d67c2b4c3d4c15829657e246d899917022e6d4d07c4382bcc3b83376d7250d85088dc73b24d030f4625fb37c5405cee04ace903d68747035fd55946ad2eb807db0b0508fc24fd54185614ab18c83127b7aa48f9927cc1258f819e02c5d2db4074736e374616664a2b49d1ff3a3effc4af201f235af5193a6e9a0192bb39aad91c5291a1b53973a85bec5dbbb3350e6c344b445c71212938d56a0c99e571bd15356979c394f84398143033fc44eb40558f253bb2445
#c=0x73658446624aaccfefa351499ece4c4635f61ff9d9d9354236afbad3b9e4000582b192f92a6e7e96b60a8899610a841faee92cb38d0e195587977cb806ecb7e4ffe8772f34cec9e0957f28040466306fe5db43b96824aa45bbebed9c1dbf15ac13db238234b60b36bded6e137483b307296e76902a13914065004a289b2186777f1c93ca656a19e751d0e7cf8c090803242ccfe14746c43fe6785028cef6380c590d59ed3469f27ac1769fa2f7fe22eace6e9af1ee33f57b120dacddabbd09239bfc133e79945af9a01568aa1e44e79813fa2e9069fb755823c4bee745f6404c1a5b690f5ba5d52c9b783bd0dfc3a4d473e99879241c0453de76be0e72980d39