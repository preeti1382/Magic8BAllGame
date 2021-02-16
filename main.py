import random

responses = ['It is certain.' , 	'Reply hazy, try again.' , 	'Don’t count on it.' ,
'It is decidedly so.' , 	'Ask again later.' , 	'My reply is no.' ,
'Without a doubt.' ,	'Better not tell you now.' , 	'My sources say no.' ,
'Yes – definitely.' , 	'Cannot predict now.' ,	'Outlook not so good.' ,
'You may rely on it.' , 	'Concentrate and ask again.' , 	'Very doubtful.' ,
'As I see it, yes.' ,		'Most likely.' , 		'Outlook good. ' ,		'Yes.',		'Signs point to yes.']

print('  __  __          _____ _____ _____    ___  ')
print(' |  \/  |   /\   / ____|_   _/ ____|  / _ \ ')
print(' | \  / |  /  \ | |  __  | || |      | (_) |')
print(' | |\/| | / /\ \| | |_ | | || |       > _ < ')
print(' | |  | |/ ____ \ |__| |_| || |____  | (_) |')
print(' |_|  |_/_/    \_\_____|_____\_____|  \___/ ')
print('')
print('')
print('')

def game():
    print("Write your question here.\n")
    question = input()
    print(responses[random.randint(0 , len(responses)-1)])
    print("I hope I helped you!\n")
    loop()

def loop():
    print("Do you want to play again? Y/N")
    reply = input().lower()
    if reply == "y":
        game()
    else:
        print("Thanks for playing!\n")

    
game()
