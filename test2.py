start = 0
end = int(input("what's the max speed?\n"))
incr = int(input("incremention num:\n"))
conv = 0.6214

print('KPH \t MPH')
print('-------------')

for kph in range(start, end + incr, incr) :
    mph = kph * conv
    print(kph, '\t', format(mph, '.1f'))


total = 0
for number in range(1,6):
    total = total + number
print(total)

while total != 0 :
    print("a")
    total = 0

