user_input = float(input("Please enter seconds: "))
if(user_input > 60 and user_input < 3600) :
    print("Minutes: ", user_input/60)
elif(user_input >= 3600 and user_input < 86400):
    print("Hours: ",user_input/3600)
elif(user_input >= 86400):
    print("Days: ",user_input/86400)