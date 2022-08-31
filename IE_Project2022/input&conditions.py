"""write a program thet recieved 3 numbers, if the sum of the 2 numbers is higher than than the hird one print a propper messge"""

first = int(input('Please enter the first number ...'))
second= int(input('Please enter the 2nd number ...'))
third= int(input('Please enter the 3rd number ...'))

print('the numbers you have entered are: {} {} {}'.format(first,second,third))
if (first+second)>third:
    print('The sum of the first two numbers is bigger than the 3rd one!!!')
if(first+second==third):
    print('the sum of the first two numbers is EQUAL to the 3rd number')
if(first==second==third):
    print('all of the numbers are equals')

else:
    print('the 3rd number is bigger than the sum of the first two number')


print('The max number is :'+ str(max(first,second, third)))
sum =first+second+third
print('the AVG is : '+str(sum/3))