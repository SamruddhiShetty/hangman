import random
dataset={5:["adopt", "maker", "table", "blood", "coast", "drove", "ought", "seven", "wrong", "zebra"], 
         6:["accept", "agency", "button", "client", "guilty", "linked", "output", "summer", "tactic", "vacant"],
         7:["accused", "barrier", "control", "healthy", "intense", "limited", "million", "perhaps", "smoking", "witness"],
         10:["dumb", "accurate", "headphones", "priority", "spectacles", "trophy", "computer", "mississippi","photoframe","trecking" ]}
print("What is your name?")
name=input()
print("Hello "+name+" welcome to Hangman")
print("choose the number of letters you would like between 5-7 or choose any size other than these")
size=input()
if int(size)==5:
    word=random.choice(dataset[5])
elif int(size)==6:
    word=random.choice(dataset[6])
elif int(size)==7:
    word=random.choice(dataset[7])
else:
    word=random.choice(dataset[10])
    
print('-'*len(word))
count=7
count1=0
l1=list(word)
l2=list('-'*len(word))
print("you can start guessing the letters, good luck!!")
while count>0 and count1!=len(word):
    x=input()
    if x not in word:
        print("wrong:(")
        count -=1
        continue
    else:
        y=l1.count(x)
        if y==1:
            index=word.index(x)
            l2[index]=x
            count1 +=1
            print("".join(l2))
        else:
            i=word.index(x)
            while y>0 and i<len(word):
                if l1[i]==x:
                    l2[i]=x
                    y -=1
                    count1 +=1
                i +=1
            print("".join(l2))
if count1==len(word):
    print("yeyy, you succesfully guessed the word")
if count==0:
    print("sorry, try again")
    print("the word was "+word)
                
                
                
                
            
            
        
        
        

