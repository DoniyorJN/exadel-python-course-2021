def narNum(num):
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
        print(num)
        
   
for i in range(0,1000):
    narNum(i)