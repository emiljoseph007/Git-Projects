name=(input("Please Enter Your Name: "))
try:
    mark=int(input("Please Enter Your Mark: "))
except ValueError:
    print("Please Enter A Valid Mark !")
else:
    print("Your Exam Results Are As Follows:")
    if mark <=14:
        print("Sorry", name ,"You Got", mark ,"You Have Failed The Exam")
    elif mark >=15 and mark <=50:
        print("Congratulations", name ,"You Got Grade C")
    elif mark >=51 and mark <=90:
     print("Congratulations", name ,"You Got A Grade B")
    elif mark >=90 and mark <=100:
     print("Congratulations", name ,"You Got A Grade A")
    elif mark==str() or mark <0 or mark >100:
     print("It Appears To Be That You Did Not Write The Exam Or You Have Entered An Invalid Mark")
    else:
     print("No Data Found")
    


