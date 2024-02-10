# Program uses a while loop to ask users their age. Program then prints the appropriate movie price.
# When user is ready to finish their session, they can type in 'end' to break the while loop.
while True:
    user_input = input("Please enter your age so I can provide accurate movie ticket prices:")
    if user_input == "end":
        break
    age = int(user_input)
    if age < 3:
        print("The movie ticket is free!")
    elif age < 13:
        print("The movie ticket price is $10.")
    else:
        print("The movie ticket price is $15.")
    
    print("Thank you for using this service! If you would like to end your session, type in 'end' without the quotation marks.")


