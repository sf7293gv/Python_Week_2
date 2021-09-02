classes_registered = ['ITEC 1150', 'ITEC 1100', 'ENGL 1340', 'MATH 1100']

only_itec = [ c for c in classes_registered if c.startswith('ITEC')]
# classes that start with ITEC
print(only_itec)

high_temps = [-1, 78, 72, 67, -1, 51, 87, 82, -1, 54, 67, 78, -1, 70]

#list of numbers with a vaild temperature measurement 

only_real_measurments = [temp for temp in high_temps if temp != -1]
print(only_real_measurments)

temp_celsius = [((temp_f - 32) * 5 / 9) for temp_f in only_real_measurments]
print(f'{temp_celsius}')

average = sum(temp_celsius) / len(temp_celsius)
print(f'The average is: {average:.1f}')

strings = ['pizza', 'lol', 'lmao']
lengths = []

for s in strings:
    length = len(s)
    lengths.append(length)

print(lengths)

# or...

lengths2 = [len(s) for s in strings]
print(lengths2)

numbers = [2, 4, 6]
plus_1 = [n+1 for n in numbers]
print(plus_1)