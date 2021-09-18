import math
while(True):
    try:
        print("Menu:")
        print("1. Calculate triangle area by base and height")
        print("2. Calculate triangle area by 2 sides and angle between them")
        print("3. Exit")
        num = int(input("Enter menu item number: "))
        area = 0        
        if(num == 1):
            a , b = input("Enter base and height:").split()
            area = int(a) *int(b) // 2
            print("Area is: " + str(area)+'\n')
        elif(num == 2):
            a, b, angle = input("Enter 2 sides and angle(degrees) between them:").split()
            area = (int(a) *int(b) * math.sin(math.radians(int(angle))))/2
            print("Area is: " + str(area)+'\n')
        elif(num == 3):
            print("Goodbye!")
            break
    except:
        print("something went wrong please enter correct value!")