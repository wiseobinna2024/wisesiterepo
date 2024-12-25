command= " "
Started= False 

while True: 
    command= input( ">").lower()
    if command=='start': 
        if Started: 
            print('The car is already started ')
        else: 
            Started= True 
            print ('The car has started!')
    elif command=='stop': 
        if not Started: 
            print( 'The car is already Stopped ')
        else: 
            Started= False 
            print('The car has stoped!')
    elif command=='help': 
        print(
            """
Start - to start the game 
Stop - to stop the game 
Quit - to quit the game 
            """
        )
    elif command=='quit': 
        break 
    else: 
        print("can't understand what you really means!")

    
