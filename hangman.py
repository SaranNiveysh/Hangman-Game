import random

hangman_doll = [
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|   |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
         |
         |
         |
    --------
    """,
    """
     -----
     |   |
         |
         |
         |
         |
    --------
    """
]
ended=False
while ended==False:
    words = [('python', 'A popular programming language'),
             ('javascript', 'The language of the web'),
             ('hangman', 'The classic word guessing game'),
             ('programming', 'What developers love to do'),
             ('developer', 'A person who writes code')]
    word, hint = random.choice(words)
    guessed_word = ['_'] * len(word)
    attempts = len(hangman_doll) - 1

    print("Welcome to Hangman!")
    print(hangman_doll[attempts])
    print("Hint: ", hint)
    print("Word: " + ' '.join(guessed_word))
    while attempts > 0 and '_' in guessed_word:
        guess = input("Guess a letter: ").lower()

        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    guessed_word[i] = guess
        else:
            attempts -= 1

        print(hangman_doll[attempts])
        print("Word: " + ' '.join(guessed_word))
        print("Attempts left: ", attempts)

    if '_' not in guessed_word:
        print("You win! The word was: ", word)
    else:
        print("You lose! The word was: ", word)
    while True:
        print("TO PLAY AGAIN ENTER Y")
        print("TO QUIT ENTER N")
        game = input("Enter your option:")
        if game in ["Y", "y"]:
            break
        elif game in ["N", "n"]:
            print("THANKS FOR PLAYING")
            ended=True
            break
        else:
            print("PLEASE ENTER A VALID OPTION")