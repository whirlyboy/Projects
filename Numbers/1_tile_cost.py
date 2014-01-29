#this program finds the cost of tiling a user-specified floor
width = float(input('Tell me the width of the floor (in m): '))
length = float(input('Tell me the length of the floor (in m): '))
cost = float(input('Tell me the cost of the tiles per square meter(in pounds): '))

print('The total cost will be £' + str(width*length*cost) + ' for ' + str(width*length) + 'm squared of flooring.')
