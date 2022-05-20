# Word Jumble
#
# The computer picks a random word and then "jumbles" it
# The player has to guess the original word

import random
"""
1. How to represent the hints? 
2. When to show the stuck user the hint?
3. How to set up the scoring system to mark for a user with or without a hint.

"""

def startGuessing():
    # create a sequence of words to choose from
    WORDS = ("python", "jumble", "easy", "difficult", "answer", "xylophone")
    hints = {"python": "a popular programming lanuage which is an animal's name",
             "jumble": " letters of words got randomly misplaced",
             "easy": "opposite word for hard",
             "difficult": "another word for 'not easy' which starts with letter 'D'",
             "answer": "responese to a question",
             "xylophone": "xylo + phone"}
    gameMessage =  """
                   Welcome to Word Jumble with Hints!

                Unscramble the letters to make a word.
               (Press the enter key at the prompt to quit.)
        """
    withHintScore = 6
    withoutHintScore = 10
    # pick one word randomly from the sequence
    word = random.choice(WORDS)
    # create a variable to use later to see if the guess is correct
    correct = word

    # create a jumbled version of the word
    # jumble(word):
    jumble = ""
    while word:
        position = random.randrange(len(word))
        jumble += word[position]
        word = word[:position] + word[(position + 1):]

    # start the game
    print(gameMessage)
    print("The jumble is:", jumble)

    guess = input("\nYour guess: ")
    needHint = ""
    withHint = False
    while guess != correct and guess != "":
        print("Sorry, that's not it.")
        needHint = getHint()
        if needHint == "yes":
            print(hints[correct])
            withHint = True
        guess = input("Your guess: ")
    if guess == correct:
        print("That's it!  You guessed it!\n")
        if withHint == True:
            score = withHintScore
        else:
            score = withoutHintScore
        print("you score is {}".format(score))

    print("Thanks for playing.")
    input("\n\nPress the enter key to exit.")

def getHint():
    print("\nDo you want the hint or not? \nplease enter yes for hint or no for no hint")
    answer = ""
    while answer.lower() not in ["yes", "no"]:
        answer = input("yes or no? ")
    return answer

if __name__ == "__main__":
    startGuessing()