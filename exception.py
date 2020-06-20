try:
    #value = 10 / 0      #zero shoule not divide any number
    number = int(input('Enter a number: '))
    print(number)
except ZeroDivisionError:
    print('Divided by zero')
except ValueError as err:
    print(err)
