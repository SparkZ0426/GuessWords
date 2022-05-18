# Word Jumble
#
# The computer picks a random word and then "jumbles" it
# The player has to guess the original word

import random
"""
1. How to represent the hints? 
2. When to show the stuck user the hint?
3. How to set up the scoring system to mark with or without a hint for a user.

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

    # pick one word randomly from the sequence
    word = random.choice(WORDS)
    # create a variable to use later to see if the guess is correct
    correct = word

    # create a jumbled version of the word
    jumble = ""
    while word:
        position = random.randrange(len(word))
        jumble += word[position]
        word = word[:position] + word[(position + 1):]

    # start the game
    print(
        """
                   Welcome to Word Jumble!

           Unscramble the letters to make a word.
        (Press the enter key at the prompt to quit.)
        """
    )
    print("The jumble is:", jumble)

    guess = input("\nYour guess: ")
    needHint = False
    withHint = False
    while guess != correct and guess != "":
        print("Sorry, that's not it.")
        print("\ndo you want the hint or not")
        needHint = input("yes(y) or no(n)")
        if  needHint.lower() == "yes":
            print(hints[correct])
            withHint = True
        guess = input("Your guess: ")
    if guess == correct:
        print("That's it!  You guessed it!\n")
        if withHint == True:
            score = 7
        else:
            score = 10
        print("you score is {}".format(score))

    print("Thanks for playing.")

    input("\n\nPress the enter key to exit.")

if __name__ == "__main__":
    startGuessing()