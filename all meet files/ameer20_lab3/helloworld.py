english= "hello world"
italian = "ciao mondo"
esperanto = "saluton mondo"
response1 = input("choose a language")

print("the translation to hello world in " + response1 + " is ")
#word english
if (response1 == "english") :
    print(english)
    else print("restart the program please")

my_name = input("what's your name?")
print("hello there, " + my_name.capitalize())
print("your name is " + str(len(my_name)) + "letters long")
print("9. first letter is: " + my_name[0].capitalize() + "last letter is: " + my_name[4].capitalize())
long_sentence = "Hi there, my name is Claire. Nice to meet you!"
print(long_sentence[21:27])
