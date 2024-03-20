count = 0
initialCount = 0

test_words = ["Hello World!","Radar","Mama?","Madam, I'm Adam.",
    "Race car!","Hannah"]
for word in test_words:
    initialCount+=1
    x = ".!?,'"
    y = "     "
    table = str.maketrans(x,y)
    #print(word.translate(table).replace(" ","").lower())
    newWord = (word.translate(table).replace(" ","").lower())
    #print(word)
    #print(newWord)
    if newWord == newWord[::-1]:
        #print(newWord)
        count+=1
        
print("Out of the",initialCount,"items,",count,"of them are palindromes.")   
print("Those items are:")   

for word in test_words:
    newWord = (word.translate(table).replace(" ","").lower())
    if newWord == newWord[::-1]:
        print(word)
        