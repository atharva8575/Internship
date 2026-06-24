import guessx

num=guessx.num
print(num)

i=1;
while i<6:
    try:

        x=int(input("Enter the number: "))
   
        if(x==num):
            print("Correct")
            break
        else:
            print("retry")
            if(i==5): 
                print("Your Chance is Our")
        
        i=i+1
    except Exception as e:
        print("Invalid input")

