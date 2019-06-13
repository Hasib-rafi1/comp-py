#Main python class
"""
This is the "guess" module.
Python class for controling user menu and Conditions.
"""
import stringDatabase
import game
import re
class guess:
    game_list = []
    limit = 100
    numbering = 1
    total_score = 0
    stringDatabaseObj = stringDatabase.stringDatabase()
    while (limit > 1):  # This constructs an infinite loop
        word = stringDatabaseObj.get_random_word()
        gameObj = game.game(numbering,word)
        guess_word = "----"
        ud_letters = word
        print("** The great guessing game ** \n")
        print("Current Word is: "+ word)
        print("Current Guess:"+ guess_word + "\n")

        condition = 1
        letter_help = 1
        while( condition == 1):
            print("g = guess, t = tell me, l for a letter, and q to quit")
            value = input("")
            if value=="g":
                user_word = input("Enter the word")
                if user_word.lower() == word.lower():
                    print("Word matched")
                    gameObj.setStatus("Success")
                    game_list.append(gameObj)
                    condition =2
                else:
                    print("Doesnt match")
                    gameObj.setBad_guess()
                    gameObj.score = gameObj.score-((gameObj.score*10)/100)

            elif value=="t":
                print("Current Word is:" + word)
                gameObj.setStatus("Gave up")
                gameObj.getUd_score()
                #print(gameObj.score)
                gameObj.score = gameObj.score - gameObj.ud_score
                #print(gameObj.score)
                #print(gameObj.ud_score)
                #print(gameObj.ud_letters)
                game_list.append(gameObj)
                condition =2
            elif value=="l":
                #print(gameObj.score)
                gameObj.score = gameObj.score/letter_help
                #print(gameObj.score)
                letter_help=letter_help+1
                user_letter = input("Enter a letter")
                if word.__contains__(user_letter):
                    gameObj.ud_letters = gameObj.ud_letters.replace(user_letter, '')

                    print("Letter is there")
                    for m in re.finditer(user_letter, word):
                        guess_word = guess_word[:m.start()] + user_letter + guess_word[m.start()+1:]  # Output: abr
                    print("Current Guess:"+ guess_word + "\n")
                else:
                    print("no match")
                    gameObj.setMissed_letters()
            elif value=="q":
                print("Game"+ '  ' +  "Word" + '  ' + "Status"+ '  ' +  "Bad Guesses" + '  ' +" Missed Letters" + '  ' + "Score")
                print("----"+ '  ' +  "----" + '  ' + "------"+ '  ' +  "-----------" + '  ' +" --------------" + '  ' + "-----")
                for gameUnit in game_list:
                    print(str (gameUnit.number)+ '     ' +  gameUnit.word + '  ' + gameUnit.status+ '       ' + str ( gameUnit.bad_guess )+ '             ' +str (gameUnit.missed_letters) + '         ' + str (float('%.2f' % (gameUnit.score))))
                    total_score = total_score + gameUnit.score
                print("Total Score :"+ str (total_score))
                condition =2
                limit = 1
        limit = limit - 1
    print ("Good bye!")
