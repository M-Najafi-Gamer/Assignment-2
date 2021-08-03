import random
print('For start the game,type \'dice\'\nif you want to exit the game,type \'exit\'')

y = 'y'
while y == 'y':
    x = input()

    if x == 'exit':
        print('hope you enjoyed the game')
        break
    
    if x == 'dice':
        dice = random.randint(1,6)

        if dice == 6:
            print('you got',dice,',now you can play your reward')
        
        if dice != 6:
            print('you got',dice,',you lose :(')
            y = input('Do you want continue(y/n)?')
