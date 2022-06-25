from random import choice

characters = "abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()"

print("\n\n================= PASSWORD GENERATOR by woken-loves-u =================\n\n")

amount = input("How many passwords do you want? \n\t >")
amount = int(amount)

pw_length = input("How long should each password be? \n\t >")
pw_length = int(pw_length)
password = ""

for i in range(amount):
    for i in range(pw_length):
        password += choice(list(characters))
        print(password)
        password = ""
