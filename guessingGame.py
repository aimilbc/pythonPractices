secret_word = 'giraffe'
guess = ''
count = 0
limit = 3
out_of_limit = False

while (secret_word != guess) and not(out_of_limit):
    if count < limit:
        guess = input('Enter guess: ')
        count += 1
    else:
        out_of_limit = True

if out_of_limit == True:
    print('You lost!')
else:
    print('You win!')
    
# using limit(for loop) with while loop, setting a boolean variable works the best
