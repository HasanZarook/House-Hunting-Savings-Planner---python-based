#House Hunting
#This code about calculate the months it will take you to save up enough money for a down
#payment

#these are the requests ask from User
annual_salary=float(input("Enter your annual salary :"))
portion_saved=float(input("enter the percentage of saved amount in your monthly salary,put this value as decimal :"))
total_cost=float(input("How cost your dream house? "))
#operators
portion_down_payment=total_cost*(0.25)  #we take the down_payment as assume
current_savings=0   #this is the ammount we save in our account when we start this funtion for calculate the months
r=0.04 #the percentage they bank give to us for our saving(annualy)
month_salary=annual_salary/12   #month salary mean,divided the annual salary by the total number of months in a year
period=0 #how many months take to save the down_payment

#function
while(current_savings<portion_down_payment):
    period=period+1
    current_savings+=(annual_salary/12)*portion_saved + current_savings*(r/12)
print("How many months will take to save the down payment :",period,"months")