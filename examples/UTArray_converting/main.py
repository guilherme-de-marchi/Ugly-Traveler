from array_manager.ut_array import *

my_array = [
    ['-', '-', '-', '-'],
    ['-', '-', '#', '-'],
    ['-', '-', '#', '-'],
    ['-', '-', '#', '-'],
]

utarray = UTArray(my_array, ['-'], ['#'])

printing = [[element.id if element != None else 0 for element in line] for line in utarray.array]
for line in printing:
    print(*line)

y = int(input('y: '))
x = int(input('x: '))
print(utarray.array[y][x].neighbors)