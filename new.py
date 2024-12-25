print('This program is to convert kelos to pound!'.upper())
first_name= input ('Please enter your first name:     ')
sur_name= input ('Please enter your sur_name:     ')
full_name= f' Mr.{ sur_name} are you ready to start the conversion?  '
print(full_name)
ans= input (' Please enter Yes or No:    '.upper())

if ans=='Yes': 
    print('Welcome to the conversion!!')
    selection= input('Please select (K) for kilos and (P) for pound:   ')
    if selection=='K':
        pound= int (input( 'Please enter the value for Pound:  '))
        result= 0.45 * pound 
        print(f'The conversion value for pound to killos is {result } kilogram')
    elif selection=='P':
        print('Your selection is to convert kilogram to pound:  ')
        kilogram= int(input( 'Please enter the value of kilogram: '))
        result= 0.45*kilogram 
        print(F'The result is {result}Pound')
        print( f'Thanks for taking part in the game Mr.{sur_name}')
elif ans== 'No': 
        print(' Okay thanks, we understand. ')
print('this is a new program!!!'.upper())
name= input('Please enter your name:   ')
print( len(name))
if len(name) <= 4: 
    print( f'{name} Please your name have to be more then 5 letters to be vaile')
elif len(name)>=25: 
    print('your name is more then 10 letters ')
else: 
    print ('YOUR NAMAE IS GREAT!')
