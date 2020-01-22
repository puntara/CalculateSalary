PayRate= 10
PayRateExtra = 15
standardHours =40
hoursWorked =50

if(hoursWorked<=standardHours):
    TotalPay1 = PayRate*hoursWorked
    print("Total Pay :",TotalPay1)
elif(hoursWorked>standardHours):
        TotalPay2= standardHours*PayRate+(hoursWorked-standardHours)*PayRateExtra
        print("Total Pay1 :", TotalPay2)