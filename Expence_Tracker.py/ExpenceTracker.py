print("Hello and welcome!")
print("Manage your expenses effortlessly, stay within budget, and achieve your financial goals with confidence.")

# print("Please Select Option")
# print("1 For Income Adding")
# print("2 For Expence Adding")
# print("3 For Availabel Balance")
# print("4 For Checking all expences")

# num=int(input("Please Select Your Option Enter Here :- "))
 
# dict={}
# match num:
#     case 1:
#         print("Enter The Income Sources")
#         source=input("Enter The Income Source name :-")
#         ammount=int(input("Enter The ammount:-"))
#         if(not source):
#             x=dict[source]
#             dict[source]=x+ammount
#         else:
#             dict[source]=ammount




# print(dict)

list=[]
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
                list.insert(1,money)
                print(list)
                           

        case 2:
                print("Enter Your Expence")
                source=input("Enter The Income Source name :-")
                ammount=int(input("Enter The ammount:-"))
                list[1]=list[1]-ammount;
                d={
                      "source":source,
                      "ammount":ammount
                }
                list.insert(2,d)
        
        case 3:
                print(f"Available balance is= {list[1]}")

        case 4:

               print("These is your total expence:")
               print(list[0])    
           
                
        case 5:
                break

print(list)