print("Hello and welcome!")
print("Manage your expenses effortlessly, stay within budget, and achieve your financial goals with confidence.")

dictincome={}
dictexpendicture={}
money=0
exp=0
i=0
j=0
while True:
    print("Please Select Option")
    print("1 For Income Adding")
    print("2 For Expence Adding")
    print("3 For Availabel Balance")
    print("4 For Checking all Income Sources")
    print("5 track all your expences")
    print("6 total expendicure")
    print("7 Clear History")
    print("8 stop")
    num=0
    try:
         num=int(input("Please Select Your Option Enter Here :- "))
         
    except Exception as e:
           print(f"Only Enter the Number {e}")

    
    match num:
        case 1:
                print("Enter The Income Sources")
                source=input("Enter The Income Source name :-")
                ammount=0
                try:
                     ammount=int(input("Enter The ammount:-"))
                except Exception as e:
                       print(f"Only Enter the Number {e}")
               
                dictincome[i]={
                       "source":source,
                      "ammount":ammount
                }
                
                money=money+ammount
                
                i=i+1
                # for key,val in dictincome.items():
                #        print(key,val)
                           

        case 2:
                print("Enter Your Expence")
                source=input("Enter The Income Source name :-")
                ammount=0
                try:
                     ammount=int(input("Enter The ammount:-"))
                except Exception as e:
                       print(f"Only Enter the Number {e}")
               
                
                dictexpendicture[j]={
                      "source":source,
                      "ammount":ammount
                }
                j=j+1
                # for key,val in dictexpendicture.items():
                #        print(key,val)
                
                exp=exp+ammount
                
                money=money-ammount
        
        case 3:
                print(f"Available balance is= {money}")

        case 4:

               print("These is Yors Income Soureces:")
               for key,val in dictincome.items():
                       print(key,val)

        case 5:
                print("These is list of total expendicture:")
                for key,val in dictexpendicture.items():
                       print(key,val) 

        case 6:   
               
               print(f"total expendicture= {exp}")
        
        case 7:
                  dictincome={}
                  dictexpendicture={}
                  money=0
                  exp=0
                  i=0
                  j=0
                
        case 8:
                break

