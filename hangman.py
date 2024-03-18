import random
def guess_game():
    wordlist = ['house','dog','cat','pneumoultrasilicovolcaniosis','hunger','biryani','bed','apple','python','blanket','pseudopseudohypoparathyroidism','identity','coding','curry','fortnite','dumplings','rice','pizza','england','glasses','monkey','money','brown','watch','show','pants','trousers','badge','future','horror','books','library','orphanage','rambunctious','lively','vivacious','keyboard','keys','sleeve','case','letters','words','brackets','aposthrophes','crazy','suprised','challenged','niger','nigeria','africa','europe','asia','oceania','australia','zipper','gray','blue','black','yellow','out','degree','upset','number','board','paddle','forgetful','forgetable','secret','experiment','thousand','hundred','million','dad','mum','godly','sky','imperative','medical','conditions','wings','fire','square','hair','ginger']
    letters_guessed = ['']
    x = random.randint(0,9)
    word = wordlist[x]
    updated_display = ''
    display = '-' * (len(word))
    attempts = 10
    guess = ''
    letters_guessed = ['']
    letter = ''

    while attempts > 0:
            print(f'\n the word is {display}.')
            
            letters_guessed.append(letter)
            letter = input('\nEnter a letter: ').lower()
            if letter == '':
                print('You have to guess something!')
                letter = input('Enter a letter: ')
            if letter == word:
                decision = input(f'Congratulations! The word was {word}, would you like to play again?').lower()
                if decision == 'no':
                        break
                else:
                    guess_game()
                
            if letter in letters_guessed:
                print('You already guessed this! Pay attention')
            elif letter != letters_guessed:
                if letter in word:
                    guess = ''
                    for i in range(len(word)):
                        if  word[i] == letter:
                            guess += letter
                        else:
                            guess += display[i]
                    display = guess
                else:
                    print('\nIncorrect!')
                    attempts -= 1
                    print(f'You have {attempts} attempts left.')
                if display == word:
                    decision = input(f'Congratulations! The word was {display}, would you like to play again?').lower()
                    if decision == 'no':
                        break
                    else:
                        guess_game()
                
                
    if attempts == 0:      
        print('\nSorry you ran out of attempts.')
        print(f'The word was {word}.')
        decision = input('Would you like to play again?')
        if decision == 'no':
            quit()
        else:
            guess_game()
        
guess_game()
    


            
            
