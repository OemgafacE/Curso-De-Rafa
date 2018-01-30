import random

print("Welcome!")
continue_program = True

while continue_program:
    print ("Choose a game:")
    print ("a) Rock Paper Scissors Lizard Spock!")
    print ("b) Guess the number!")
    print ('Write "quit" to quit the programm')

    game = input ()

    if game == "quit":
        print("Shuting down...\nThanks for playing!")
        continue_program = False
    
    elif  game == "a":
        
        print ("Welcome to RPSLS!")
        print ("The first who gets 5 points wins!")
        
        continue2 = True
        score = [0,0]
        
        def scorePrint ():
            print("You", score[0], "/ AI", score[1])
       
        
        while continue2 :
                 
                print("Choose between \nrock paper scissors lizard spock")
                print('Write "quit" to leave this game.')
                
                player = input()
                enemy = random.randint (0,4)
                
                if player == "quit":
                    continue2 = False
                
                weapons = ["rock", "paper", "scissors", "lizard", "spock"]
                enemy = weapons[enemy]
                fin = ["You won!", "You lose..."]
                
                def win ():
                    print(fin[0])
                    score[0] += 1
                    scorePrint()
                    
                def lose ():
                    print(fin[1])
                    score[1] +=1
                    scorePrint()
            
                if player != "quit":
                    print(player, "vs", enemy)            
                
                if enemy == player:
                   print ("It's a draw!")
                   scorePrint()
                
                elif player == "rock":
                    if  enemy == "scissors" or enemy == "lizard" :
                        win()
                    else :
                        lose() 
             
                elif player == "paper":
                    if  enemy == "rock" or enemy == "spock" :
                        win()
                    else :
                        lose()
               
                elif player == "scissors":
                    if  enemy == "lizard" or enemy == "paper" :
                        win()
                    else :
                         lose()
                
                elif player == "lizard":
                    if  enemy == "spock" or enemy == "paper" :
                        win()
                    else :
                         lose()
             
                elif player == "spock":
                    if  enemy == "scissors" or enemy == "rock" :
                        win()
                    else :
                        lose()
                
                else:
                    print("Wait, what? Thats not valid!")
                    lose()
                
                if score[0] == 5:
                    print("You won the game!")
                    continue2 = False
                    
                elif score[1] == 5:
                    print("The AI wins the game!")
                    continue2 = False
               
    elif  game == "b":
        print("Welcome to Guess The Number!")
        print("Guess a random number between 1 and 100  in 10 turns or less.")

        continue2 = True
        turns = 10
        
        while continue2 :
            
            #Al rear las siguientes funciones y ponerlas en su lugar,
            #el programa no funcionaba bien, por lo que simplemente repeti codigo.
            
            #def end():
            #    turns = 0
            #def quit():
            #     continue 2 = False
     
            turns = 10
            print('Write "quit" to leave the game.')

            number = random.randint(1, 100)
            
            while turns > 0 :
                print("Which number is it?")   
                player = input ()
                
                if player == "quit":
                 #end()
                    turns = 0
                #quit() 
                    continue2 = False
                        
                else:
                    player = int(player)
                
                    if player == number:
                        print("You won!\nLet's play again!")
                    #end()
                        turns = 0
                        
                    elif player < number:
                        print("Nope, its higher...")
                        
                    elif  player > number:
                        print("Nope, its lower...")
                            
                    turns -= 1
                        
                    if turns > 0:
                        print("You have", turns, "turn/s left.")
                    
                    elif turns == 0:
                        print("There are no more turns left, you lose...\nLet's play again!")
    
    else:
        print("Not a valid input, try again.")