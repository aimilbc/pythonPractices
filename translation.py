# this program translate vowels to 'g'

def translate(phrase):
    translation = ''
    for letter in phrase:
        if letter in 'AEIOUaeiou':      # also can use "if letter.lower() in 'aeiou': "
            if letter.isupper():
                translation = translation + 'G'
            else:
                translation = translation + 'g'
        else:
            translation = translation + letter
    return translation

# print(translate(input('Enter a phrase: ')))   # Open importFiles.py to see how it works
