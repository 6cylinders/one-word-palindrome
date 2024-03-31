
import math


def is_palindrome(userInput):

    userInputDisplay = userInput
    userInput = userInput.replace(" ", "")
    strLength = len(userInput)
    center = math.ceil(strLength/2)

    if strLength % 2 == 0:

        firstHalf = userInput[0:center]
        secondHalf = userInput[-center:]

    else:

        firstHalf = userInput[0:center-1]
        secondHalf = userInput[-center+1:]

    if firstHalf.lower() == secondHalf.lower()[::-1]:
        return (f"{userInputDisplay} is a palindrome!")

    else:
        return (f"{userInputDisplay} isn't a palindrome")


userInput = input("Enter a word here: ")
while userInput.lower() != "done":
    print(f"\n{is_palindrome(userInput)}")
    userInput = input("Enter a word here: ")
