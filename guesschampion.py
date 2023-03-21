def computer():
    from random import randint

    user_hp=100
    system_hp=100
    print("\t### THE GUESS CHAMPION ###\t")
    print("\n>This is a number guessing game.")
    print("\n>In the first round your opponent will  pick a random number from 1 to 50. Your job is to guess it. "
          "\nThe closer you guess, higher the damage on the opponent.  ")
    print("\n>In the next round you will choose a number from 1 to 50 and your opponent will guess it."
          "\nThe closer the guess, higher the damage on you.")
    print("\n>The game will continue until either you or your opponent runs out of HP.")
    print("\n\t ___POINTS BREAKDOWN___\n")
    print(">Exact guess:- 100 damage\n>Within the difference of 5:- 50 damage\nWithin the difference of 10:- 25 damage\n"
          ">Within the difference of 20:- 10 damage\n>Anything else 0 damage")

    print("\nYOUR HP: 100"
          "\nOPPONENT HP: 100")
    turn=1
    while user_hp>0 and system_hp>0:

        if turn%2 != 0:
            print("\nYOUR OPPONENT HAS PICKED A NUMBER")
            sys_random=randint(1,51)
            guess=int(input("Guess the number:  "))
            print(f"\nOpponent pick: {sys_random}")
            print(f"Your guess: {guess}")
            if sys_random==guess:
                system_hp-=100
                print("\nFATALITY!!!\nYOU guessed right.\nYour opponent was dealt with a 100 DAMAGE")
                print("\n\t ---YOU WON---")
                break
            elif -5<=sys_random-guess<=5 and sys_random!=guess:
                system_hp -= 50

                print("\nBRAVO!\nYou dealt your opponent 50 damage")
                if system_hp > 0:
                    print(f"OPPONENT HP: {system_hp}")
                    print(f"YOUR HP: {user_hp}")
                else:
                    print("\n\t ---YOU WON---")
                    break
            elif -10<=sys_random-guess<=10 and sys_random!=guess:
                system_hp -= 25
                print("\nGood!\nYou dealt your opponent 25 damage")
                if system_hp > 0:
                    print(f"OPPONENT HP: {system_hp}")
                    print(f"YOUR HP: {user_hp}")
                else:
                    print("\n\t ---YOU WON---")
                    break
            elif -20<=sys_random-guess<=20 and sys_random!=guess:
                system_hp -= 10
                print("\nYou dealt your opponent 10 damage")
                if system_hp > 0:
                    print(f"OPPONENT HP: {system_hp}")
                    print(f"YOUR HP: {user_hp}")
                else:
                    print("\n\t ---YOU WON---")
                    break
            else:

                print("\nOOF!!\nYou missed.")
                if system_hp > 0:
                    print(f"OPPONENT HP: {system_hp}")
                    print(f"YOUR HP: {user_hp}")
            turn+=1
        if turn % 2 == 0:
            print("\nYOU WILL PICK A NUMBER")
            sys_random = randint(1, 51)
            guess = int(input("Pick a number:  "))
            print(f"\nYour pick: {guess}")
            print(f"Opponent guess: {sys_random}")
            if sys_random == guess:
                user_hp-= 100
                print("\nFATALITY!!!\nYour opponent guessed right.\nYou were dealt with a 100 DAMAGE")
                print("\n\t---YOU LOST---")
                break

            elif -5 <= sys_random - guess <= 5 and sys_random != guess:
                user_hp -= 50
                print("\nUNLUCKY!\nYou were dealt with 50 damage")
                if user_hp > 0:
                    print(f"OPPONENT HP: {system_hp}")
                    print(f"YOUR HP: {user_hp}")
                else:
                    print("\n\t---YOU LOST---")
                    break
            elif -10 <= sys_random - guess <= 10 and sys_random != guess:
                user_hp -= 25
                print("\nOH! MY!\nYou were dealt with 25 damage")
                if user_hp > 0:
                    print(f"OPPONENT HP: {system_hp}")
                    print(f"YOUR HP: {user_hp}")
                else:
                    print("\n\t---YOU LOST---")
                    break
            elif -20 <= sys_random - guess <= 20 and sys_random != guess:
                user_hp -= 10
                print("\nYou were dealt with  10 damage")
                if user_hp > 0:
                    print(f"OPPONENT HP: {system_hp}")
                    print(f"YOUR HP: {user_hp}")
                else:
                    print("\n\t---YOU LOST---")
                    break
            else:

                print("\nWOO!! YOU GOT LUCKY\n He missed.")
                if user_hp > 0:
                    print(f"OPPONENT HP: {system_hp}")
                    print(f"YOUR HP: {user_hp}")
            turn += 1



