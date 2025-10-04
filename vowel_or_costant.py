word=input("enter the words in lower case: ")
vowels="aeiou"
if len(word)!=1:
    print("enter the correct lower case word")
elif word in vowels:
    print(f"the word{word} is a vowel.")
else :
    print(f"the word {word} is a constant")