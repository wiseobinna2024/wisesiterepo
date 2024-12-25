print('This is a guessing game: '.upper())
right_guess= 8
guess_count= 0 
guess_limit= 3

while guess_count < guess_limit: 
    guess= int(input("Please enter your Guess:  "))
    guess_count+=1 
    if guess==right_guess: 
        print("You won!!")
        break 
    else: 
        print ('wrong selection please try again ')
else: 
    print ('Sorry you lost. ')
    