import copy
# using shallow copy and deep copy need to import copy file

print('---------- using equal sign ----------')
original_1 = [1, 2, 3, 4, 5]

print('= sign isn''t copying the original list, it''s creating a pointer(reference) to the original list')
num1 = original_1
print('num1 = original_1')
print('original_1: ' + str(original_1))
print('id of num1: ' + str(id(original_1)))
print('original_1: ' + str(num1))
print('id of num1: ' + str(id(num1)))

print('\nonce we changed new_num, original will also changed.')
num1.append(6)
print('num1.append(6)')
print('original_1: ' + str(original_1))
print('num1: ' + str(num1))

print('\n---------- using shallow copy(copy.copy) ----------')
original_2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print('shallow copy(copy.copy()) will copy ONLY the object, but STILL referencing elements')
num2 = copy.copy(original_2)
print('num2 = copy.copy(original_2)')
print('original_2: ' + str(original_2))
print('id of num2: ' + str(id(original_2)))
print('original_2: ' + str(num2))
print('id of num2: ' + str(id(num2)))

print('\neven we changed object, it won''t affect original_2 IF WE ONLY CHANGE OBJECT')
num2[0] = ['a', 'b', 'c']
print('num2[0] = [a, b, c]')
print('original_2: ' + str(original_2))
print('num2: ' + str(num2))
num2 = copy.copy(original_2)    # resetting the change

print('\nBUT if we changed element, it will affect original_2 because elements are STILL referencing the original')
num2[0][2] = 'd'
print('num2[0][2] = d')
print('original_2: ' + str(original_2))
print('num2: ' + str(num2))

print('\n---------- using deep copy(copy.deepcopy) ----------')
original_2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print('deep copy(copy.deepcopy()) will create a copy, so these two will be independent')
num3 = copy.deepcopy(original_2)
print('num3 = copy.deepcopy(original_2)')
print('original_2: ' + str(original_2))
print('id of num3: ' + str(id(original_2)))
print('original_2: ' + str(num3))
print('id of num3: ' + str(id(num3)))

print('\neven we changed object or element, it won''t affect original_2')
num3[0] = ['a', 'b', 'c']
print('num3[0] = [a, b, c]')
print('original_2: ' + str(original_2))
print('num3: ' + str(num3))
num3 = copy.copy(original_2)    # resetting the change
num3[0][2] = 'd'
print('num3[0][2] = d')
print('original_2: ' + str(original_2))
print('num3: ' + str(num3))