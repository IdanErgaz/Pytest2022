""" play with lists methods"""
cars=['BMW', 'HYUNDAI', 'SUBARU', 'PEGOT', 'SEAT']
print('Thcars length is : '+str(len(cars)))
print(sorted(cars))
print('the 3rd car index is :' + cars[3])
cars[2]= 'HONDA'
print('cars 2nd index new name is:'+ cars[2])
cars.append('DACHIA')
print(cars)
print('deleting subaru')
cars.remove('PEGOT')
print('the new cars list after DELETING PEGOT')

print(cars)
print(cars.count('PEGOT'))

x= input('please insert a car name')
if x in cars:
    print("The car {} is in the cars list and can be found in index: {}".format(x, str(cars.index(x))))
else:
    print('The car you HAVE INSERTED is NOT part of the list !!!')