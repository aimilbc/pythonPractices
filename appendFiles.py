# if you use 'w', it basically overwrites the file, so gotta be CAREFUL!
# if you want to create a new file, simply put a new file name in open() so python will automatically creates one.

memo_file = open('/Users/aimi/Desktop/memo.txt','a')

memo_file.write('Aimi''s file!!!')

memo_file.close()               # MAKE SURE CLOSE THE FILE!!!!
