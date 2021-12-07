#TL = Thomas li
#AB = Alexander Berardi
#ET = Ernest Tang
#YJC = You Jia Chuang
import random
import time

# print an introductory statement
def displayIntro():
    playAgain = "No"
    print('''You are an intrepid Adventurer who seeks wealth and riches. Unfortunately, you have to go through a dangerous dragon infested cave in order to succeed.
You have trekked many miles to reach the mouth of a cave fabled for its danger and adventure. As you enter the cave you are
confronted with a fork in the path. Each path leads to a different cave. One of the paths (Cave 1) is darkly lit and covered in cobwebs and dead vines.
The other (Cave 2) is clean and well maintained, almost as if someone has been there before. Which one will you choose?''')


# You Jia
#import time
def it_is_fun():
    print('''You have been walking for a long time and are starting to feel very thirsty, so you decide to make yourself a drink
There are six compounds in front of you,
you have to figure out which two compounds will produce water
after reaction in order to survive.''')
# This is a introductory line
    time.sleep(8)
    print("Ready...")
    time.sleep(2)
    print("Go!")
    print("""
The compounds are:
CuO,Ag,NaOH,CO2,CaSO4,HCl
""")
# The 6 given compounds

def choose_compounds_a():
    a=""
    while a!='CuO'and a!='Ag'and a!="NaOH"and a!="CO2"and a!="CaSO4"and a!="HCl":
        print("Which one compound is your choice 1: ")
        a=input()
    return a
# This is the line asks user to type their first input
def choose_compounds_b():
    b=""
    while b!='CuO'and b!='Ag'and b!="NaOH"and b!="CO2" and b!="CaSO4" and b!="HCl":
        print("Which one compound is your choice 2: ")
        b=input()
    return b
# This is the line that asks user to type their second input (choice)

# tf() is the name of my final function
def tf():
    (it_is_fun())
    x=choose_compounds_a()
    y=choose_compounds_b()
    print("Your answer is...")
    time.sleep(2)
    print("Wait...")
    if x!="NaOH" and x!="HCl":
        print("Water...")
        time.sleep(2)
        print("Water...")
        time.sleep(2)
        print("You die of thirst")
        print('Do you want to play again? (yes or no)')
        playAgain = input()
        # Here check whether the user type the right compound or not for the first input
        #return None
    elif y!="NaOH" and y!="HCl":
        print("Water...")
        time.sleep(2)
        print("Water...")
        time.sleep(2)
        print("You die of thirst")
        print('Do you want to play again? (yes or no)')
        playAgain = input()
        # Here check whether the user type the right compound or not for the second input
        #return None
    elif y==x:
        print("Water...")
        time.sleep(2)
        print("Water...")
        time.sleep(2)
        print("You die of thirst")
        print('Do you want to play again? (yes or no)')
        playAgain = input()
        # Here check whether the user type same compounds for the first and second input
        #return None
    else:
        print("Water...")
        time.sleep(2)
        print("YEAH!!!")
        print("Lots of water coming out of the cave!!!")
        return True

        # Alex Berardi's cypher game
def ComboSolver(): #This function sees if the user input matches the randomly generated cypher. If so, the person proceeds, if not, they die and are returned to the beginning (AB)
    x=random.randint(1,9) #The random integers are generated to be input into the introductory string (AB)
    y=random.randint(1,9)
    z=random.randint(1,9)
    b=random.randint(1,9)
    #This is the introductory string, where the x,y,z,b random integers are input. The user has to read the text in order to succeed (AB)
    print('You have entered a dark cavern filled with moss and rock formations. You see', (x), 'stalagmites,',(y),'stalactites,',(z),'different species of moss, and',(b),'bats hanging from the cavern ceiling. At the end of the cave you see a small but solid looking door. As you approach the door you see that it is sealed with a small combination lock on the front. This combination lock has 4 numbers that need to be input. This needs to be unlocked in order to proceed, how will you unlock it? ')
    First = (input('What is the First number? ')) #This queries the user for input to solve the question (AB)
    Second = (input('What is the Second number? '))
    Third = (input('What is the Third number? '))
    Fourth = (input('What is the Fourth number? '))
    if First.isdigit(): #This asks if the user input is a digit (AB)
        First=int(First) #If it is a digit, this turns it into an int value so that it can be compared with an if statement (AB)
    else: #These 4if/else statements make sure that the program kills you if you input something that isn't a digit (AB)
        return False
    if Second.isdigit():
        Second = int(Second)
    else:
        return False
    if Third.isdigit():
        Third = int(Third)
    else:
        return False
    if Fourth.isdigit():
        Fourth = int(Fourth)
    else:
        return False
    if First == x: #Booleans that decide if user input matches the cypher (AB)
        if Second == y:
            if Third == z:
                if Fourth == b:
                    print("The door Unlocked!") #The player proceeds (AB)
                    return True
    else:
         return False #This kills the player and asks if they want to go back to the start (AB)

#Ernest Tang
#Hangman
def hangman_game():
    #List of possible words (ET)
    word_list = ("skull", "rubble", "hermit", "limestone", "exploration", "passageway", "tarantula", "burial", "abyss", "caveman")
    #Life check function (ET)
    def life_check(lives):
        if lives > 1:
            print("Try again!")
        elif lives == 1: #Give player a free letter if only one life left (ET)
            hint_status = input("A rat appears and asks if you want a hint. Take the hint? Type \"yes\" or \"y\" for hint. ")
            if hint_status == "yes" or hint_status =="y":
                hint = "_"
                while hint == "_":
                    hint = word[random.randint(-1,len(word))]
                while hint in word:
                    character_index = word.index(hint)
                    space[character_index] = hint
                    word[character_index] = "_"
            else:
                return
        elif lives == 0: #Player loses (ET)
            return False


    #Introductory message (ET)
    print("You enter the cave and a magical blackboard appears on a wall!")

    #Select a random word from list (ET)
    original_word = list(word_list[random.randint(0, 9)])
    word = original_word

    #Message for the player (ET)
    print(str(len(word)) + " spaces appear on the wall. Try inputting a character!")

    #Create space to display to player (ET)
    space = list("_" * len(word))

    #Number of lives (ET)
    lives = 6

    #Check if letters are remaining and if player has lives (ET)
    while "_" in space and lives > 0:
        print(space)
        guess = input("Guess a letter: ")
        if len(guess) != 1 or guess.isalpha() == False: #If input is invalid (ET)
            print("Your input is invalid!")
            lives = lives - 1
            print("You have " + str(lives) + " lives remaining.")
            life_check(lives)
            continue
        elif guess not in word: #If guess is wrong (ET)
            print("That letter is not part of the word! Try again.")
            lives = lives - 1
            print("You have " + str(lives) + " lives remaining.")
            life_check(lives)
            continue
        elif guess in word: #If guess is correct (ET)
            while guess in word:
                character_index = word.index(guess)
                space[character_index] = guess
                word[character_index] = "_"
            continue

    #If player has guessed all letters (ET)
    if "_" not in space:
        print(space)
        print("You win! A hole in a wall opens up to an undiscovered path and allows you to continue on your journey.")
        return True

##Thomas Li's Game:


def tictactoe():
    '''
    This function allows you to play goblin tic tac toe
    '''
    def drawBoard(board):
        '''
        (list) --> str
        '''
        #TL This function's purpose is to create the tic tac toe board
        #TL each -, +. and / divides the board up
        #TL the indexed board lists will be the spaces that eventually hold the symbols

        print(board[7] + '|' + board[8] + '|' + board[9])
        print('-+-+-')
        print(board[4] + '|' + board[5] + '|' + board[6])
        print('-+-+-')
        print(board[1] + '|' + board[2] + '|' + board[3])

    def inputPlayerLetter():
        '''
        #TL () --> list (This takes inputs from the user)
        '''
        #TL This function lets the user choose which symbol they are going to be
        letter = ''
        print('Do you want to be X or O?')


        #TL The .upper() method will convert lower case answers into uppercase strings
        #TL which the program can understand
        letter = input().upper()

        #TL If the user does not enter an X or O, the goblin will prompt the user
        #TL to do so
        while not (letter == 'X' or letter == 'O'): #TL
            print('The goblin laughs. That\'s not an X or an O buddy.') #TL
            letter = input().upper()

        #TL In the given list, the first element will be read as the player's and the second
        #TL one will be the computers. This is interpreted by a later function.
        if letter == 'X':
            return ['X', 'O']
        else:
            return ['O', 'X']

    def whoGoesFirst():
        '''
        () --> str
        '''
        #TL This function will randomly choose which player goes first.
        if random.randint(0, 1) == 0:
            return 'goblin'
        else:
            return 'player'

    def makeMove(board, letter, move):

        #TL This function changes the value of an element in a list.

        board[move] = letter

    def isWinner(bo, le):
        '''
        (list, str) --> bool
        '''
        #TL This function determines winning boards. If specific elements of the board list are filled, the function will return true.
        #TL In this case, it occurs when two corners and the center
        #TL are occupied by the same sign
        #TL bo will stand for board and le will stand for letter
        return ((bo[1] == le and bo[5] == le and bo[3] == le) or
                # TL The bottom two corners + center
        (bo[1] == le and bo[5] == le and bo[7] == le) or # TL Left corners + middle
        (bo[7] == le and bo[5] == le and bo[9] == le) or # TL top corners + middle
        (bo[9] == le and bo[5] == le and bo[3] == le)) # TL Right corners + middle


    def isWinner_1(bo, le):
        '''
        (list, str) --> bool
        '''
        # TL This is another winning board position
        # TL In this case, the winning pattern is some 45 degree rotation of
        # TL filling in spaces [1],[4], and [8]. In other words, an upsidedown
        # TL L block on the left side without its bottom connecting square
        return ((bo[1] == le and bo[4] == le and bo[8] == le) or # TL The left side
        (bo[7] == le and bo[8] == le and bo[6] == le) or #TL The top side
        (bo[9] == le and bo[6] == le and bo[2] == le) or #TL the right side
        (bo[3] == le and bo[2] == le and bo[4] == le)) #TL The bottom side


    def isWinner_2(bo, le):
        '''
        (list, str) --> bool
        '''
        #TL This is another winning board position
        #TL In this case, the winning pattern is some 45 degree rotation of
        #TL filling in spaces [2],[4], and [7]. In other words, a
        #TL L block on the left side without its bottom connecting square
        return ((bo[2] == le and bo[4] == le and bo[7] == le) or #TL The left side
        (bo[4] == le and bo[8] == le and bo[9] == le) or #TL The top side
        (bo[8] == le and bo[6] == le and bo[3] == le) or #TL The right side
        (bo[6] == le and bo[2] == le and bo[1] == le)) #TL The bottom

    def isWinner_3(bo, le):
        '''
        (list, str) --> bool
        '''
        #TL This is another winning board position
        #TL These winning positions entail occuping two corners and the middle space
        #TL opposite the two corners
        return ((bo[1] == le and bo[3] == le and bo[8] == le) or #TL Bottom two corners
        (bo[7] == le and bo[1] == le and bo[6] == le) or #TL Left two corners
        (bo[7] == le and bo[9] == le and bo[2] == le) or #TL Top two corners
        (bo[9] == le and bo[3] == le and bo[4] == le)) #TL Right two corners

    #TL Randomized variable to be used in the next function
    x = random.randint(1, 4)


    #TL This function will randomize the winning conditions, and that way each
    #TL play-through of this game will be different
    #TL This is done using the random.randint method used in the x variable
    def winning_cond(bo, le):

        if x == 1:
            return isWinner(bo, le)

        elif x == 2:
            return isWinner_1(bo, le)

        elif x == 3:
            return isWinner_2(bo, le)

        elif x == 4:
            return isWinner_3(bo, le)




    def getBoardCopy(board):
        '''
        (list) --> list
        '''
        #TL board copy is a new list that will be filled by a pre-existing board
        #TL this is mostly going to be used for the AI to do calculations
        boardCopy = []
        for i in board:
            boardCopy.append(i)
        return boardCopy

    def isSpaceFree(board, move):
        '''
        (list, int) --> bool
        '''
        #TL This function returns True if the move argument is free on the board argument
        #TL Free spaces in the board list would have ' ' as its element.
        return board[move] == ' '

    def getPlayerMove(board):
        '''
        (list) --> int
        '''
        #TL This function will ask the user for an input move
        move = ' '
        print('What is your next move? (1-9)')
        move = input()

        #TL The next statement checks to see if the user inputted a valid move in
        #TL tic-tac-toe
        while move not in '1 2 3 4 5 6 7 8 9'.split() \
            or not isSpaceFree(board, int(move)):
            print('The goblin giggles sheepishly. That\'s not a valid move. Are you joking me?(1-9)')
            move = input()
        return int(move)

    def chooseRandomMoveFromList(board, movesList):
        '''
        (list, list) --> int
        '''

        #TL This function checks to see if there are any possible moves.
        #TL It does this by checking if there are still empty spaces in the
        #TL board list fed into function. If the length of the empty space
        #TL list is longer than zero then there are still moves to be made.
        possibleMoves = []
        for i in movesList:
            if isSpaceFree(board, i):
                possibleMoves.append(i)

        if len(possibleMoves) != 0:
            return random.choice(possibleMoves)
        else:
            return None

    def getComputerMove(board, computerLetter):
        '''
        (list, int) --> int
        '''


        #TL This next section serves as the algorithm for the Tic-Tac-Toe AI:
        #TL The AI first checks to see if it can win the next turn
        for i in range(1, 10): #TL The computer will output a result from 1-9
            boardCopy = getBoardCopy(board) #TL A copy of the board is generated for analysis
            if isSpaceFree(boardCopy, i): #TL Checks to see if a space is free
                makeMove(boardCopy, computerLetter, i) #TL The move is made on the copy of the board
                if winning_cond(boardCopy, computerLetter): #TL Checks to see if making the move results in a win
                    return i #TL If making the move results in a win then the move is returned
        #TL Note some of the previous functions only make an appearance in the computer AI function

        #TL In an effort to make the AI more beatable its AI got tweaked. The computer
        #TL will not check to see if the user can win in one move
        #TL Instead, they will place their symbol in one of the sides, as their next
        #TL option if they can not immediately win.
        move1 = chooseRandomMoveFromList(board, [2, 4, 6, 8])
        if move1 != None:
            return move1

        #TL Next the computer will try to take one of the corners, if they are free.
        move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
        if move != None:
            return move



        #TL Finally the computer will try to take the center.
        return 5



    def isBoardFull(board):
        '''
        (list) --> bool
        '''
        # TL this function checks to see if the board is full.
        #TL if none of the elements of the board list in the range of 1-9 are spaces
        #TL then the function will return true
        for i in range(1, 10):
            if isSpaceFree(board, i):
                return False
        return True


    #TL This is where the defined functions end and the game actually begins

    #TL This print statement deals with the goblin explaining some rules.
    print('\nYou take the well lit path, and the straw crunches nicely under your boots.')
    time.sleep(2)
    print('\nHowever, just as you are about to see the glimpse of some treasure, a goblin ermerges from the shadows.')
    time.sleep(4)
    print('\nInstead of attacking you immediately he challenges you to a game.')
    time.sleep(2.5)
    print('\n\n\"Today we play goblin tic tac toe.\"\n He says.')
    time.sleep(2.2)
    print('\n\n\"The rules are simple, we play up to seven games of tic tac toe, if you can beat me in even one game of tic tac toe I will let you go. ')
    time.sleep(4)
    print('\nHere\'s the catch, 3 in a row might not be the way to win. You have seven tries to figure out what the winning pattern of x\'s and o\'s are, and to beat me with that knowledge. ')
    time.sleep(5)
    print('\nYou\'re just a pathetic human, so I\'ll even give you a hint. For any winning pattern, a rotation by 45 degrees of the same pattern is also a winning pattern.')
    time.sleep(5)
    print('\nNow that being said... ')
    time.sleep(1)
    print('\nIf you don\'t beat me,')
    time.sleep(1)
    print('\nI EAT you! ')
    time.sleep(1)
    print('\nExcited?\"\n ')
    time.sleep(0.75)
    print('--'*16)
    time.sleep(0.5)
    print('\nChills run up your spine...\n\nYou prepare to play some of the greatest tic tac toe of your life.')
    time.sleep(3)
    print('\n\nQuick instructions: Please input an integer between 1-9 to place your symbol.\
     1-3 correspond to the bottom row from left to right respectively.\
    The same logic applies for 4-6 for the middle row, and 7-9 for the top row\n\n')
    time.sleep(8)

    #TL This for loop will run this goblin tic-tac-toe game up to 7 times.
    for i in [1,2,3,4,5,6,7]:

        #TL Some exiciting print statements, and time.sleep methods to kick us off.
        #TL The time.sleep methods create delays between print messages
        print('This is round ' + str(i) + '. There are seven rounds maximum')
        time.sleep(2)
        print('The challenge proceeds in 3')
        time.sleep(0.75)
        print('                          2')
        time.sleep(0.5)
        print('                          1')
        time.sleep(0.5)

        #TL Everytime a new round starts the board needs to be cleared
        #TL that is why the entries are replaced by spaces
        theBoard = [' '] * 10

        #TL The imputPlayerLetter() function creates a list containing an x and an o and the elements of this
        #TL list are assigned to the variable playerLetter and computerLetter.
        #TL In short, the player will decide whether they are x or o.
        playerLetter, computerLetter = inputPlayerLetter()

        #TL randomized who goes first
        turn = whoGoesFirst()
        print('A flip of a coin determines that the ' + turn + ' will go first.')

        ##TL Only keep playing if the game is a tie
        gameIsPlaying = 'Tie or Loss'

        #TL The previous for loop ensures that at most 7 rounds of tic-tac-toe will be played
        #TL This while loop ensures that a round of tic tac toe will be completed.
        #TL It will loop everytime a person/computer makes a move. Thus the game
        #TL will not freeze after one move is made.
        while gameIsPlaying == 'Tie or Loss':
            if turn == 'player':
                #TL This section is the player's turn
                drawBoard(theBoard)
                move = getPlayerMove(theBoard)
                makeMove(theBoard, playerLetter, move)

                #TL If you win, you exit the while loop
                if winning_cond(theBoard, playerLetter):
                    drawBoard(theBoard)
                    gameIsPlaying = 'You have won'
                    break #TL Exit while loop/round of tic-tac-toe
                else:
                    if isBoardFull(theBoard):
                        drawBoard(theBoard)
                        print('This round was a tie!')
                        time.sleep(1)

                        break #TL exit the while loop
                    else:
                        turn = 'goblin'

            else:
                #TL This section is the computer's turn
                move = getComputerMove(theBoard, computerLetter)
                makeMove(theBoard, computerLetter, move)

                if winning_cond(theBoard, computerLetter):
                    drawBoard(theBoard)
                    print('The Goblin Laughs as he wins!')
                    time.sleep(1)

                    break #TL Exit while loop/round of tic-tac-toe
                else:
                    if isBoardFull(theBoard):
                        drawBoard(theBoard)
                        print('This round was a tie!')
                        time.sleep(1)

                        break #TL Exit while loop/round of tic-tac-toe
                    else:
                        turn = 'player'




        ##TL If you win any round of tic tac toe the entire game ends.
        #TL The break will cause you to exit the for loop and you will
        #TL not need to play all 7 rounds
        if gameIsPlaying == "You have won":
            print('Hooray! You have beat the goblin\'s challenge! The goblin allows you to pass.')
            break


    ##TL These returns feed into the overall game checking to see if you progress or not.
    if gameIsPlaying != "You have won":
        return False


    if gameIsPlaying == "You have won":
        return True
##-----------------------------------------


playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y': #loops the entire game if the player answers "yes" or "y" to any play again message (ET)
    displayIntro()
    print('You approach the cave...')
    time.sleep(2)
    checkFirstCave = input("Which cave will you go into? (1 or 2) ")
    while checkFirstCave not in ("1", "2"):
        checkFirstCave = input("Please type in valid input: ")
    if checkFirstCave == "1":
        FirstCave = ComboSolver()
        if FirstCave == True: #Each function outputs True when the player wins so they are able to advance to the next cave, and loss condition and prompts are included in the functions (ET)
            checkSecondCave = input("You pass through the first cave without incident, but you soon find yourself with another decision to make. After a little bit of walking, you are faced with another two caves. One (Cave 1) is overgrown with moss and vines, it almost looks like a miniature jungle had taken root in this dark cave complex. The other (Cave 2) is dark and damp but relatively clear, and you can see some sort of light at the end of it. Which cave will you go into? (1 or 2) ")
            while checkSecondCave not in ("1", "2"):
                checkSecondCave = input("Please type in valid input: ")
            if checkSecondCave == "2":
                SecondCave = hangman_game()
                if SecondCave == True:
                    ThirdCave = tf()
                    if ThirdCave == True:
                        checkFinalCave = input("You get a feeling that you are nearing the end, for better or worse. You come up on a final fork in the path that leads to two caves. One cave (Cave 1) is brightly lit and you can hear the faint echos of evil sounding laughter. The second cave (Cave 2) has a path that is obviously well used. The floor is covered in straw and you can smell burnt pine, almost as if someone has a fire burning further into the cave. Which cave will you go into? (1 or 2) ")
                        while checkFinalCave not in ("1", "2"):
                            checkFinalCave = input("Please type in valid input: ")
                        if checkFinalCave == "2":
                            FinalCave = tictactoe()
                            if FinalCave == True:
                                print("You finally stumble into a cave that is filled with gold and gems. You are now richer than the most wealthy of kings. Good Job Adventurer!")
                                print('Do you want to play again? (yes or no) ')
                                playAgain = input()
                            else:
                                print('Your seven chances are up, the goblin eats you...') #TL
                                print('Do you want to play again? (yes or no)') #TL
                                playAgain = input() #TL Local playAgain variables inside our functions didn't translate to the global setting so we needed more else statements
                        else:
                            print("You wander down the path to the first cave, as the laughter gets louder you can see small, man-like shadows reflected in the torchlight. Eventually you come upon a cavern filled with evil little goblins. They all turn as one and glare at you with beady red eyes. They then proceed to tear you appart with a variety of very sharp weapons. The End.")
                            print('Do you want to play again? (yes or no) ')
                            playAgain = input()
                else:
                    print ("The rat opens a trap door and you fall through the floor!")
                    print('Do you want to play again? (yes or no)')
                    playAgain = input()
            else:
                print("You walk into the underground jungle. The heavy vegetation pushes against you making it tough going. You decide to use your sword to cut through the vines to help you travel. The jungle does not like this. Instantly you are attacked my a monsterous venus flytrap with very sharp teeth. It chomps you in half with ease. The End.")
                print('Do you want to play again? (yes or no) ')
                playAgain = input()
        else:
            print("It didn't work! You hear a deep rumbling from above you. You must have triggered a booby trap! A boulder falls from the ceiling and crushes you. The End") #This is the death statement for ComboSolver (AB)
            print('Do you want to play again? (yes or no) ') #This asks if you want to restart for Combosolver (AB)
            playAgain=input()
    else:
        print('You walked into a dragon sleeping in a pitch-black cave and woke him up! You died.')
        print('Do you want to play again? (yes or no) ')
        playAgain = input()
