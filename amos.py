
#this project will calculate total amount of money gained after investment for 3 years
def money_investment():

    print("YOUR ARE MOST WELCOME TO NATION BANK OF MALAWI")
    print()

    #allowing user to invest his or her  money
    principle_1=int(input("you should invest 100,000:"))
    if principle_1==100000:
        #calculating interest and add it to first principle entered by user(first year)
        interest_1=principle_1*1*0.05
        principle_2=principle_1+interest_1

        #calculating interest and add it to second principle (second year)
        interest_2=principle_2*1*0.05
        principle_3=principle_2+interest_2

        #calculating interest and add it to third principle(third year)
        interest_3=principle_3*1*0.05
        principle_4=principle_3+interest_3

        #printing  amount of money after 3 years
        print("your money after 3 years will be:  k",principle_4)
    else:
        print("you have intered large money or small money , please check")

money_investment()
