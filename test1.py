usr_input= True
while usr_input==True:
    try:
        usr_input2= int(input('Enter an integer:'))  
        if usr_input2 > 0 :
            print(usr_input2**2)
            usr_input= False
        else: 
            print('Sorry, I only work with positive integers.')
    except:
        print('Error: You did not enter an integer.')
print('End of Program')