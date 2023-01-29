#my_string = input("Input a word to reverse: ")

#for char in range(len(my_string) -1, -1, -1):
#    print(my_string[char], end="")

def reverseWord(Word):
    words = Word.split(" ")
    newWords = [word[::-1] for word in words]
    newWord = " ".join(newWords)
    return newWord

Word = "Can't stop me"
print(reverseWord(Word))