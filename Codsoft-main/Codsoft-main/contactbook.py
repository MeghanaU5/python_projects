names = []
phone_numbers = []

num = 3

for i in range(num):
    name = input("enter name: ")
    phone_number = input("enter phone number: ")

    names.append(name)
    phone_numbers.append(phone_number)


print("\tNames\t\t\tPhone Number")

for i in range(num):
    print(f'\t{names[i]}\t\t\t{phone_number[i]}')

s = input("enter the name to search: ")
if s in name:
    index = names.index(s)
    name = names[index]
    phone_number = phone_numbers[index]

    print(f"Name:{name} , Phone Number:{phone_number}")
else:
    print("Name not found!.....")