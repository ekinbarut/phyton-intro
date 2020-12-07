str_num = int(input('Starting number of organisms: '))
avg_di = str(input('Avarage daily increase (%) : '))
nm_odtm = int(input('Number of days to multiply: '))
print('Day','\t' ,'Approximate Population')
for nm_odtm in range(1, nm_odtm + 1):
    avg_di = avg_di.replace("%", "")
    avg_di_int = int(avg_di)
    calc = (1 + avg_di_int/100)**(nm_odtm - 1) * str_num
    calc=round(calc,6) 
    print(nm_odtm, '\t', calc)