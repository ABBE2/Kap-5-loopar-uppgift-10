print(' Temperatur tabell ')
print('===================')
print('Celcius\tFarenheit')

i = 40
while i >= -40:
    print(i,'\t', int(i*9/5+32))
    i -= 1