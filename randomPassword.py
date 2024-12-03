import random
import string

pass_len=int(input("Enter No N to Generate Random Password Of Length N : "))

charValue=string.ascii_letters+string.digits+string.punctuation

password="";
for i in range(pass_len):
    password+=random.choice(charValue)

print("Your Random Password of Length "+str(pass_len)+" is "+ password)