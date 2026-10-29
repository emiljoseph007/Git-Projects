bill_amount=float(input("Please Enter Your Total Bill:"))
tip_percentage=float(input("Please Enter The Tip Percentage You Want To Give:"))
tip=bill_amount*tip_percentage/100
total=bill_amount+tip
print("/------THE GRAND BUDAPEST-----/" \
"RECIEPT")
print("Your Total Bill:", bill_amount)
print("Tip Percentage You Entered:", tip_percentage)
print("GRAND TOTAL:", total)
print("-----THANK YOU-----")