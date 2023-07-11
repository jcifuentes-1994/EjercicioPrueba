
import random as rd

num = "0123456789"
alfanum = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
guion = "-"
nif = rd.sample(num,8) + rd.sample(guion,1) + rd.sample(alfanum,3)
nifFinal = "".join(nif)
print(nifFinal)