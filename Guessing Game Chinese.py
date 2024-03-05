import secrets

number = secrets.SystemRandom().randint(1,101)

guessthenumber = 0



while True:
    guessthenumber = int(input("輸入數字："))

    if guessthenumber < 1 or guessthenumber >100:
        print("您只能輸入1到100之間的數字！")

    elif guessthenumber == number:
        print("得左")


    elif guessthenumber > 10:
        print("Warm, 數字大於10")
        print(number)
    elif guessthenumber < 10:
        print("Cold,數字少於10")
        print(number)
