#!/usr/bin/env python

def ekin():
    file_contents = open('numbers.txt', 'w')
    num_list = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
    for num in num_list:
       file_contents.write(str(num) + '\n')
    file_contents.close()
    file = open('numbers.txt', 'r')
    total=0
    line_count = 0
    for x in file:
        total += int(x)
        line_count+=1
    file.close()
    
    average = total/line_count
    print('Average: ', average)
    file.close()
    return average
ekin()