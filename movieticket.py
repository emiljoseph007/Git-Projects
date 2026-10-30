how_many=int(input("How Many Tickets Do You Want To Buy:"))
names=[]
total=0
for person in range(how_many):
    name=input("Please Enter Your Name:")
    age=int(input("Please Enter Your Age:"))
    if age < 12:
        value=100
    elif age >65:
        value=150
    else:
        value=250
    total+=value
    names.append(name)
print("Your Final Ticket Price Is:", total)
print("Names of ticket holders:", names)