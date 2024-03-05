import secrets

number = secrets.SystemRandom().randint(1,101)

guessthenumber = 0



while True:
    guessthenumber = int(input("Enter the number: "))

    if guessthenumber < 1 or guessthenumber >100:
        print("You can enter the number between 1 to 100 only!")

    elif guessthenumber == number:
        print("Bongo")



    elif guessthenumber > 10:
        print("Warm")
        print(number)
else:
        print("Cold")
        print(number)





