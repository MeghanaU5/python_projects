import random,string

lower=string.ascii_lowercase
upper=string.ascii_uppercase
digits=string.digits
symbols=string.punctuation

while True:
    pass_len=int(input("enter length of the password:"))

    if pass_len<8:
        print("password length should be more than 8.")
        continue
    else:
        break

characters=lower+upper+digits+symbols

password=""

for i in range(pass_len):
    password+=random.choice(characters)

print("Password Generated is",password)