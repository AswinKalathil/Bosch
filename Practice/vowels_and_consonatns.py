vowels = "aeiouAEIOU"
vowelsCount=0
vowelsList=[]
consonantsCount = 0
consonantsList =[]

string = input("Enter a String:")\

for ch in string:
    if not ch.isalpha():
        continue
    elif ch in vowels:
        vowelsCount+=1
        vowelsList.append(ch)
    else:
        consonantsCount +=1
        consonantsList.append(ch)
        
print("In String"+string+"\n")

print("Number of Vowels :",vowelsCount," ",vowelsList)   
print("Number of Consonants :",consonantsCount," ",consonantsList)       
    

