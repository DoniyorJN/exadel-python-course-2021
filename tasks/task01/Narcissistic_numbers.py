def narNum(num):
    if(num >= 1 and num <= 1000):
        result = 0
        division = 1
        length = 0 
        while(True):
            division *= 10
            length += 1
            if(num//division==0):
                break
        for i in range(length):
            division //= 10
            result +=  (num//division%10) ** length
        if(result == num):
            print("This is Narcissistic number")
        else:
            print("This is NOT Narcissistic number")
    else:
        print("please enter number between 1 and 1000")

narNum(1634)