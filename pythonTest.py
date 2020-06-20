#checking Palindrome
x = input('Enter any sequence')
y = x[::-1]
if x == y:
    print('Palindrome')
else:
    print('Not a palindrome')

#displaying pyramids
def new_left(a):
    for x in range(a):
        print(''*(a-x-1)+'*'*(2*x+1))
new_left(5)

def new_center(a):
    for x in range(a):
        print(' '*(a-x-1)+'*'*(2*x+1))
new_center(5)

def new_right(a):
    for x in range(a):
        print('  '*(a-x-1)+'*'*(2*x+1))
new_right(5)


#python stores as string, needed to convert to int or float
num1 = input('Number 1: ')
num2 = input('Number 2: ')
print(float(num1) + float(num2))


#lists
friends = ['Vanessa','Leana','Michael','Anthony','Olivia','Brian','Efrain',2020,True]
print(friends)      #print all elements
print(friends[0])   #print only Vanessa
print(friends[-1])  #print the last element
print(friends[1:])  #print from Leana
print(friends[0:7]) #print Vanessa[0] - Efrain[6]
print('\n')


#list functions
lucky_nums = [4,6,7,9,27,87,76,3,33,44]
friends = ['Vanessa','Leana','Michael','Anthony','Olivia','Brian','Efrain',2020,True]
friends.extend(lucky_nums)  #adds up friends + nums lists
print('extend:')
print(friends)

friends.append('Allen')     #added to the last element
print('append:')
print(friends)

friends.pop()               #popped the last element
print('pop:')
print(friends)

friends.insert(1,'Kelly')   #Kelly will be at index 1, and from Leana will push back
print('insert:')
print(friends)

friends.remove(1)           #deleting 'True' element because True = 1, False = 0
print('remove(1):')
print(friends)

friends.remove('Kelly')     #deleting 'Kelly'
print('remove(''Kelly''):')
print(friends)

print(friends.count('Vanessa'))

friends.reverse()           #reversing the elements
print(friends)

lucky_nums.sort()              #sorting the elements
print(lucky_nums)

friends2 = friends.copy()
print(friends2)
friends3 = friends
print(friends3)

friends.clear()             #clear the lists
print('clear:')
print(friends)
print('\n')

      
#tuples
coordinates = (8,4)         #tuples using (), lists using []. Tuples can't modify elements, but lists can.
print(coordinates[1])


#functions for python
def say_hi():
    print('Hello Aimi!')
say_hi()

def greeting(name):
    print('Hello ' + name + ', how are you?')
name = input('Enter your name: ')
greeting(name)
#greeting(12)            # Python takes number as int when we pass as a parameter, but stores in variable as string

def cube(num):
    return num*num*num
print(cube(2))


#if statements
is_male = True
if is_male:
    print('You are male\n')
else:
    print('You are not male\n')

is_tall = False
if is_male or is_tall:
    print('You are male or tall or both\n')
elif is_male and not(is_tall):
    print('You are short male\n')
elif not(is_male) and is_tall:
    print('You are not a male and are tall\n')
else:
    print('You are neither male nor tall\n')

is_tall = True
if is_male and is_tall:
    print('You are tall male\n')
else:
    print('You are neither not male or not tall\n')


#comparison
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num3:
        return num2
    else:
        return num3
print(max_num(3,7,4))








