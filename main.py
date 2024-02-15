import random as rd
digits="0123456789"
small_alphabets="abcdefghijklmnopqrstuvwxyz"
capital_alphabets="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_characters="!@#$&+-/*|\?<>,.%"

#To generate a random characters
def generate_password():
    digit=rd.choice(digits)
    small=rd.choice(small_alphabets)
    capital=rd.choice(capital_alphabets)
    special=rd.choice(special_characters)
    combine=[digit,small,capital,special]
    char=rd.choice(combine)
    return char

#Main Funciton 
if __name__=="__main__":
    print("\t\t\t"+"-"*33)
    print("\t\t\t\tPASSWORD GENERATOR")
    print("\t\t\t"+"-"*33)
    password_length=int(input("Enter password length: "))
    #if password length is less than 8
    while(password_length<8):
        print("The minimum password length is 8 ")
        password_length=int(input("Enter password length: "))
    password=""
    for i in range(password_length):
        character=generate_password()
        password+=character
    print("The password : "+password)