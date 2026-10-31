word=input("Please Enter The Word Or Sentence")
vowels="aeiouAEIOU"
ch=0
for character in word:
    if character in vowels:
        ch+=1
print("num of vowels" , ch)