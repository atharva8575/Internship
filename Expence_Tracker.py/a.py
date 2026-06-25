print("Hello and welcome!")
print("Manage your expenses effortlessly, stay within budget, and achieve your financial goals with confidence.")



list=[]
listexp=[]
money=0
while True:
    print("Please Select Option")
    print("1 For Income Adding")
    print("2 For Expence Adding")
    print("3 For Availabel Balance")
    print("4 For Checking all expences")
    print("5 stop")
    num=int(input("Please Select Your Option Enter Here :- "))

    
    match num:
        case 1:
                print("Enter The Income Sources")
                source=input("Enter The Income Source name :-")
                ammount=int(input("Enter The ammount:-"))
                d={
                      "source":source,
                      "ammount":ammount
                }
                list.insert(0,d)
                money=money+ammount
                print(list)
                           

        case 2:
                print("Enter Your Expence")
                source=input("Enter The Income Source name :-")
                ammount=int(input("Enter The ammount:-"))
                money=money-ammount
                d={
                      "source":source,
                      "ammount":ammount
                }
                listexp.insert(0,d)
                money=money-ammount;
        
        case 3:
                print(f"Available balance is= {money}")

        case 4:

               print("These is your total expence:")
               for key,val in list[0].items():
                      print(f"{key} , {val}")    
           
                
        case 5:
                break

print(list)