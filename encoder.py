def encode(password1):
    tempstr = ""
    for i in password1:
        temp = int(i)+3
        if temp > 9:
            temp%=10
        tempstr+=str(temp)
    return tempstr

def main():
    password = ""
    store1 = ""
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        choice = input("Please enter an option: ")
        if choice == "1":
            password = input("Please enter your password to encode: ")
            store1 = encode(password)
            print("Your password has been encoded and stored!")

        elif choice == "2":
           store2 = decode(store1)
            print("The encoded password is ", store1, ", and the original password is ", store2, sep = "")

        elif choice == "3":
            break

if __name__ == "__main__":
    main()

